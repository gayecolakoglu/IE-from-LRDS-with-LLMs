# run_pipeline.py

import json
import os
from os import path
import re
import time
import requests
import logging
import pandas as pd
from modules.data_processing import load_dataset, get_markdown_files_by_template, extract_text_from_markdown, process_ground_truth_annotations
from modules.chunking import get_chunk_size, generate_chunk
from modules.prompt_generation import generate_prompt
from modules.batch_processing import sanitize_filename, generate_custom_id
from modules.postprocessing import reconcile_predictions
from modules.evaluation import evaluate_response_with_metrics
from config import MODEL_llama, few_shot_examples

def perform_experiment(directory, base_output_directory, dataset_path, dtype, folder_path,  model, sample_size, use_custom_ocr, experiment_id, prompt_type, chunk_size_category, output_file=None, **kwargs):
    logging.info(f"Starting experiment with ID {experiment_id}")
    try:
        example_num = kwargs.get('example_num', None)
        no_schema = kwargs.get('no_schema', True)
        transformation_method = kwargs.get('transformation_method', 'naive')
        chunking_method = kwargs.get('chunking_method', 'fixed')
        overlap = kwargs.get('overlap', None)
        level_type = kwargs.get('level_type', 'STL')

        template_types = ['Amendment', 'Dissemination', 'Short-Form']
        categorized_files = get_markdown_files_by_template(folder_path, level_type)
        ground_truth_annotations, _ = load_dataset(dataset_path) if model == MODEL_llama else (None, None)
        
        output_data = []
        existing_custom_ids = set()
        filename_mapping = {}
        task_counter = 0
        
        for template_type in template_types:
            files_list = list(categorized_files[level_type][template_type])
            sample_files = files_list[:sample_size]
            examples = few_shot_examples[level_type][template_type][example_num] if not no_schema and example_num else None
            
            for filepath in sample_files:
                filename = os.path.basename(filepath)
                start_time = time.time()
                logging.info(f"Experiment {experiment_id}: Processing file {filename}")
                
                success = False
                retry_count = 0
                max_retries = 10
                sanitized_filename, original_filename = sanitize_filename(filename)
                filename_mapping[sanitized_filename] = original_filename 
                
                while not success and retry_count < max_retries:
                    try:
                        with open(filepath, 'r', encoding='utf-8') as file:
                            markdown_content = file.read()
                        
                        extracted_data = extract_text_from_markdown(markdown_content)
                        chunk_size = get_chunk_size(chunk_size_category, prompt_type, example_num)
                        logging.info(f"Generating chunks for file {filename}")
                        chunks, prompt_token_size = generate_chunk(chunking_method, extracted_data, chunk_size, overlap)
                            
                        if not chunks:
                            logging.error(f"Chunk generation failed for file {filename}")
                            break
                            
                        if model == MODEL_llama:
                            file_predictions = process_chunks(
                                chunks, prompt_type, examples, template_type, level_type,
                                MODEL_llama, dtype, example_num
                            )
                            if not file_predictions:
                                raise ValueError(f"No valid predictions obtained for file {filename} after retries.")
                                break
                            reconciled_predictions = reconcile_predictions(file_predictions)
                            filename_pdf = os.path.splitext(filename)[0] + '.pdf'
                            ground_truth = process_ground_truth_annotations(filename_pdf, ground_truth_annotations)
                            evaluated_results = evaluate_response_with_metrics(reconciled_predictions, ground_truth)
                        else:
                            for page_num, chunk in enumerate(chunks):
                                chunk_content = chunk['text'] + ' ' + chunk['layout'] if isinstance(chunk, dict) else chunk
                                prompt = generate_prompt(dtype, prompt_type, chunk_content, examples, template_type, level_type, example_num)
                                custom_id = generate_custom_id(experiment_id, level_type, template_type, sanitized_filename, prompt_type, example_num, chunk_size_category, transformation_method, page_num, task_counter)
                                
                                while custom_id in existing_custom_ids:
                                    task_counter += 1
                                    custom_id = generate_custom_id(experiment_id, level_type, template_type, sanitized_filename, prompt_type, example_num, chunk_size_category, transformation_method, page_num, task_counter)
                                
                                existing_custom_ids.add(custom_id)
                                task_counter += 1
                                
                                request_body = {
                                    "model": model,
                                    "temperature": 0.0,
                                    "messages": [
                                        {"role": "system", "content": "You are an LLM that extracts information from given document. Provide the extracted values in JSON format."},
                                        {"role": "user", "content": str(prompt)}
                                    ],
                                }
                                task = {"custom_id": custom_id, "method": "POST", "url": "/v1/chat/completions", "body": request_body}
                                
                                if output_file:
                                    with open(output_file, "a") as file:
                                        file.write(json.dumps(task) + "\n")
                        
                        success = True
                        experiment_result = {
                            "experiment_id": experiment_id,
                            "model_name": model,
                            "sample_num": len(sample_files),
                            "chunking_method": chunking_method,
                            "chunk_size": chunk_size,
                            "overlap": overlap,
                            "prompt_type": prompt_type,
                            "example_num": example_num,
                            "prompt_token_size": prompt_token_size,
                            "level_type": level_type,
                            "template_type": template_type,
                            "transformation_method": transformation_method,
                            "file_name": original_filename
                        }
                        if model == "llama":
                            experiment_result.update({
                                "ground_truth": json.dumps(ground_truth),
                                "predictions": json.dumps(reconciled_predictions) if reconciled_predictions else json.dumps({}),
                                **evaluated_results
                            })
                        output_data.append(experiment_result)
                            
                    except requests.exceptions.HTTPError as e:
                        handle_rate_limit(e, retry_count)
                    except Exception as e:
                        logging.error(f"An error occurred while processing file {filename}: {e}")
                        break

        if model == MODEL_llama:
            experiment_file_path = os.path.join(base_output_directory, 'experiments2')
            output_file = os.path.join(experiment_file_path, f"experiment_{experiment_id}_results.csv")
            pd.DataFrame(output_data).to_csv(output_file, index=False)
            logging.info(f"Experiment {experiment_id}: Results written to {output_file}")
            return pd.DataFrame(output_data)

    except Exception as e:
        logging.error(f"Error during experiment {experiment_id}: {e}")
        if model == MODEL_llama:
            return pd.DataFrame()
        return {}, []
    return filename_mapping, output_data

def run_experiment(directory, base_output_directory, dataset_path, dtype, folder_path,  model, params, output_file=None):
    sample_size, use_custom_ocr, prompt_type, chunk_size_category, kwargs, experiment_id = params
    if model == MODEL_llama:
        try:
            result = perform_experiment(directory, base_output_directory, dataset_path, dtype, folder_path,  model, sample_size, use_custom_ocr, experiment_id, prompt_type, chunk_size_category, **kwargs)
            return result
        except Exception as e:
            logging.error(f"An error occurred in experiment {experiment_id}: {e}")
            return pd.DataFrame()

    else:
        try:
            filename_mapping, output_data = perform_experiment(directory,  base_output_directory, dataset_path, dtype, folder_path,  model, sample_size, use_custom_ocr, experiment_id, prompt_type, chunk_size_category, output_file, **kwargs
            )
            if output_data:
                logging.info(f"Experiment {experiment_id} completed successfully.")
            else:
                logging.warning(f"Experiment {experiment_id} did not return any results.")
            return experiment_id, filename_mapping, output_data
        except Exception as e:
            logging.error(f"An error occurred in experiment {experiment_id}: {e}")
            return experiment_id, {}, []

def test_experiment_serially(directory, base_output_directory, dataset_path, dtype, folder_path,  model, experiment_params, output_file=None):
    if model == MODEL_llama:
        for i, params in enumerate(experiment_params):
            try:
                result = run_experiment(directory, base_output_directory, dataset_path, dtype, folder_path,  model, params)
                if not result.empty:
                    print("Experiment completed successfully.")
                else:
                    print("Experiment did not return any results.")
            except Exception as e:
                print(f"Experiment resulted in an exception: {e}")
        
    else:
        all_experiment_mappings = {}
        all_experiment_output_data = {}
        
        for i, params in enumerate(experiment_params):
            try:
                experiment_id, filename_mapping, output_data = run_experiment(directory, base_output_directory, dataset_path, dtype, folder_path,  model, params, output_file)
                all_experiment_mappings[experiment_id] = filename_mapping
                all_experiment_output_data[experiment_id] = output_data
                if output_data:
                    print(f"Experiment {experiment_id} completed successfully.")
                else:
                    print(f"Experiment {experiment_id} did not return any results.")
            except Exception as e:
                print(f"Experiment {experiment_id} resulted in an exception: {e}")
        
        with open(os.path.join(base_output_directory, "all_filename_mappings.json"), "w") as f:
            json.dump(all_experiment_mappings, f, indent=4)
        
        with open(os.path.join(base_output_directory, "all_output_data.json"), "w") as f:
            json.dump(all_experiment_output_data, f, indent=4)
            
        return all_experiment_mappings, all_experiment_output_data

def load_experiment_results(base_output_directory):
    # Define the paths to the JSON files
    filename_mappings_path = os.path.join(base_output_directory, "all_filename_mappings.json")
    output_data_path = os.path.join(base_output_directory, "all_output_data.json")

    # Load the filename mappings from the JSON file
    with open(filename_mappings_path, "r") as f:
        all_filename_mappings = json.load(f)

    # Load the output data from the JSON file
    with open(output_data_path, "r") as f:
        all_output_data = json.load(f)

    return all_filename_mappings, all_output_data