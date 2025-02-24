# batch_processing.py

import json
import os
import re
import pandas as pd
import openai
from openai import OpenAI
from modules.evaluation import evaluate_response_with_metrics
from modules.postprocessing import reconcile_predictions
from modules.data_processing import process_ground_truth_annotations
from config import api_key_gpt
from typing import List, Dict
import logging

openai.api_key = api_key_gpt
client = openai.OpenAI(api_key=api_key_gpt)

def split_jsonl_file(input_file_path, max_size=209715200, max_lines=1000):
    base_name = os.path.splitext(input_file_path)[0]
    file_number = 0
    current_lines = []
    current_size = 0
    
    with open(input_file_path, 'r', encoding='utf-8') as infile:
        for line in infile:
            line_size = len(line.encode('utf-8'))
            if len(current_lines) >= max_lines or (current_size + line_size) > max_size:
                output_file_path = f"{base_name}_part{file_number}.jsonl"
                with open(output_file_path, 'w', encoding='utf-8') as outfile:
                    outfile.writelines(current_lines)
                current_lines = []
                current_size = 0
                file_number += 1
            current_lines.append(line)
            current_size += line_size

        if current_lines:
            output_file_path = f"{base_name}_part{file_number}.jsonl"
            with open(output_file_path, 'w', encoding='utf-8') as outfile:
                outfile.writelines(current_lines)

    return [f"{base_name}_part{i}.jsonl" for i in range(file_number + 1)]

def send_batch_requests(batch_file_paths):
    batch_ids = []
    for batch_file_path in batch_file_paths:
        with open(batch_file_path, "rb") as f:
            batch_input_file = client.files.create(
                file=f,
                purpose="batch"
            )
        batch_input_file_id = batch_input_file.id

        batch = client.batches.create(
            input_file_id=batch_input_file_id,
            endpoint="/v1/chat/completions",
            completion_window="24h",
            metadata={
                "description": f"batch processing job {os.path.basename(batch_file_path)}"
            }
        )
        
        batch_ids.append(batch.id)
    return batch_ids

def check_batch_status(batch_ids):
    batch_statuses = {}
    for batch_id in batch_ids:
        batch_status = client.batches.retrieve(batch_id)
        batch_statuses[batch_id] = batch_status
    return batch_statuses

def process_batch_responses_local(file_path, ground_truth_annotations, filename_mapping, experiment_output_data, base_output_directory, experiment_id):
    with open(file_path, 'r', encoding='utf-8') as f:
        file_content = f.read()
        
    all_predictions = {}
    for line in file_content.splitlines():
        try:
            response = json.loads(line)
        except json.JSONDecodeError:
            logging.error(f"Invalid JSON format in line: {line}")
            continue


        custom_id = response['custom_id']
        parts = custom_id.split('|')
        response_experiment_id = int(parts[0])
        sanitized_filename = parts[3]

        if response_experiment_id != int(experiment_id):
            continue

        if sanitized_filename not in filename_mapping:
            logging.error(f"Sanitized filename '{sanitized_filename}' not found in mapping for experiment ID {experiment_id}.")
            continue 

        original_filename = filename_mapping[sanitized_filename]
        if not original_filename:
            logging.error(f"Failed to retrieve original filename for sanitized filename '{sanitized_filename}' in experiment ID {experiment_id}.")
            continue 
        
        try:
            message_content = response['response']['body']['choices'][0]['message']['content']
            message_content_cleaned = re.sub(r'```json|```', '', message_content).strip()
            parsed_content = json.loads(message_content_cleaned)
            
            if isinstance(parsed_content, list):
                # Append each item from the list to all_predictions
                for item in parsed_content:
                    all_predictions.setdefault(sanitized_filename, []).append(item)

            else:
                # Handle case when parsed_content is a dictionary
                all_predictions.setdefault(sanitized_filename, []).append(parsed_content) # -> dict[str, list[dict]]

            # The keys are the sanitized filenames (sanitized_filename, which are strings).
            # The values are lists of parsed JSON objects (parsed_content).

        except json.JSONDecodeError:
            logging.error(f"Invalid JSON format in message_content for custom_id {custom_id}: {message_content}")
            continue 

    for sanitized_filename, predictions in all_predictions.items():
        reconciled_predictions = reconcile_predictions(predictions)
        original_filename = filename_mapping.get(sanitized_filename)
        
        if original_filename:
            if not original_filename.endswith(".pdf"):
                if original_filename.endswith("pdf"):
                    original_filename = original_filename[:-3] + ".pdf"
                else:
                    original_filename += ".pdf"

            # Add to `experiment_output_data`
            ground_truth = process_ground_truth_annotations(original_filename, ground_truth_annotations)

            evaluated_results = evaluate_response_with_metrics(reconciled_predictions, ground_truth)


            # Update or append entry
            existing_entry = next((entry for entry in experiment_output_data if entry["file_name"] == original_filename), None)
            if existing_entry:
                existing_entry.update({
                    "ground_truth": json.dumps(ground_truth),
                    "predictions": json.dumps(reconciled_predictions or {}),
                    **evaluated_results
                })
            else:
                experiment_output_data.append({
                    "file_name": original_filename,
                    "ground_truth": json.dumps(ground_truth),
                    "predictions": json.dumps(reconciled_predictions or {}),
                    **evaluated_results
                })

            logging.info(f"Processed and saved reconciled predictions for {original_filename}")
        else:
            logging.error(f"Original filename not found for sanitized filename '{sanitized_filename}'.")

    # Write experiment results to CSV
    experiment_file_path = os.path.join(base_output_directory, 'experiments')
    os.makedirs(experiment_file_path, exist_ok=True)
    result_file = os.path.join(experiment_file_path, f"experiment_{experiment_id}_results.csv")
    result_df = pd.DataFrame(experiment_output_data)
    result_df.to_csv(result_file, index=False)
    logging.info(f"Experiment {experiment_id}: Results written to {result_file}")

def retrieve_and_process_batch_results(response_dir, ground_truth_annotations, all_filename_mappings, all_output_data, base_output_directory):
    for experiment_id, filename_mapping in all_filename_mappings.items():
        if int(experiment_id) < 96:
            experiment_output_data = all_output_data.get(experiment_id, [])
            for filename in os.listdir(response_dir):
                if filename.endswith(".jsonl"):
                    file_path = os.path.join(response_dir, filename)
                    process_batch_responses_local(
                        file_path, ground_truth_annotations,
                        filename_mapping, experiment_output_data, base_output_directory, experiment_id
                    )

def sanitize_filename(filename):
    sanitized = filename.replace(" ", "_").replace(",", "").replace("(", "").replace(")", "").replace("&", "").replace("'", "").replace("\"", "").replace(".", "").replace("/", "").strip()
    return sanitized, filename

def generate_custom_id(experiment_id, level_type, template_type, sanitized_filename, prompt_type, example_num, chunk_size_category, transformation_method, page_num, task_counter):
    # Create a hash to ensure the custom_id is unique
    unique_string = f"{experiment_id}|{level_type}|{template_type}|{sanitized_filename}|{prompt_type}|{example_num}|{chunk_size_category}|{transformation_method}|{page_num}|{task_counter}"
    # unique_hash = hashlib.md5(unique_string.encode()).hexdigest()
    # return f"{experiment_id}_{level_type}_{template_type}_{filename}_{page_num}_{unique_hash}"
    return unique_string