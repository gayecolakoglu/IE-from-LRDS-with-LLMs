# model_interaction.py

from groq import Groq
import re
import time
import random
import logging
from requests.exceptions import HTTPError
from modules.rate_limiters import RateLimiter, GlobalRateLimiter
from modules.postprocessing import parse_model_output, parse_model_output_ad
from modules.prompt_generation import generate_prompt, prompt_token_length_function
from config import api_key_gpt, api_key_llama
import openai
from openai import RateLimitError
from typing import List, Dict
# from httpx import HTTPError
from tenacity import retry, stop_after_attempt, wait_exponential
from threading import Lock

global_rate_limiter = GlobalRateLimiter(max_tokens_per_minute=6000)
rate_limiter = RateLimiter(max_tokens_per_minute=6000)
lock = Lock()

class RateLimitError(Exception):
    """Custom exception for rate limit errors."""
    pass

def parse_reset_time(reset_time_str):
    """Convert reset time string like '3s' or '191' to seconds."""
    try:
        if reset_time_str.endswith('s'):
            return int(reset_time_str[:-1])
        return int(reset_time_str)
    except ValueError:
        return 0

def handle_rate_limit(headers, retry_count):
    """Handle rate limiting based on headers."""
    retry_after = float(headers.get("retry-after", 0))
    remaining_tokens = int(headers.get("x-ratelimit-remaining-tokens", 0))
    reset_time = parse_reset_time(headers.get("x-ratelimit-reset-tokens", "0s"))

    if retry_after:
        logging.info(f"Retrying after {retry_after:.2f} seconds.")
        time.sleep(retry_after)
    elif remaining_tokens == 0:
        logging.info(f"No tokens left. Cooling down for {reset_time} seconds.")
        time.sleep(reset_time)
    else:
        delay = min(2 ** retry_count + random.uniform(0, 5), 120)
        logging.info(f"Adaptive delay of {delay:.2f} seconds due to rate limit.")
        time.sleep(delay)

def parse_retry_after(error_details):
    """Parse retry-after time from error details."""
    retry_after = error_details.get('error', {}).get('retry_after', None)
    if retry_after:
        try:
            return float(retry_after)
        except ValueError:
            return None

    message = error_details.get('error', {}).get('message', "")
    match = re.search(r"try again in ([\d.]+)s", message)
    return float(match.group(1)) if match else None

def random_request_delay():
    """Introduce a random delay between requests."""
    delay = random.uniform(1, 3)
    logging.info(f"Random delay of {delay:.2f} seconds before making a request.")
    time.sleep(delay)

def adaptive_delay(retry_count):
    """Adaptive delay using exponential backoff with jitter."""
    delay = min(2 ** retry_count + random.uniform(0, 5), 120)
    logging.info(f"Adaptive delay of {delay:.2f} seconds due to rate limit feedback.")
    time.sleep(delay)
    return delay

def run_conversation(prompt, model):
    api_key = ""
    """Handles a single conversation with specified model."""
    if model in ["gpt-4o", "gpt-3.5-turbo"]:
        api_key = api_key_gpt
        openai.api_key = api_key
        client = openai.OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "You are an LLM that extracts information from PDFs and uses the data extracted to answer specific questions. Provide the extracted values in JSON format."
                },
                {
                    "role": "user",
                    "content": str(prompt),
                }
            ],
            max_tokens=4096,
        )
        if response.choices:
            return response.choices[0].message.content
        logging.error("No response choices returned from model.")
        return None

    elif model == "llama3-70b-8192":
        api_key = api_key_llama
        client = Groq(api_key=api_key)
        messages = [
            {
                "role": "system",
                "content": "You are an LLM that extracts information from PDFs and uses the data extracted to answer specific questions. Provide the extracted values in JSON format."
            },
            {
                "role": "user",
                "content": str(prompt),
            }
        ]
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=4096
        )
        return response.choices[0].message.content

    else:
        raise ValueError(f"Unsupported model: {model}")

@retry(stop=stop_after_attempt(10), wait=wait_exponential(multiplier=1, min=4, max=60))
def run_conversation_with_retry(prompt, model):
    """Wrapper to handle rate-limiting and retries."""
    retry_count = 0
    while True:
        try:
            prompt_tokens = prompt_token_length_function(prompt)
            if rate_limiter:
                rate_limiter.request_tokens(prompt_tokens)
            if global_rate_limiter:
                global_rate_limiter.request_tokens(prompt_tokens)

            with lock:
                return run_conversation(prompt, model)

        except HTTPError as e:
            if e.response.status_code == 429:
                retry_count += 1
                logging.warning("Rate limit error encountered.")
                handle_rate_limit(e.response.headers, retry_count)
            else:
                logging.error(f"HTTP error while processing prompt: {e}")
                raise
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            raise

        if retry_count > 10:
            raise RateLimitError("Max retries exceeded for run_conversation due to rate limits.")

def process_chunks(chunks, prompt_type, examples, template_type, level_type,
                   MODEL, dtype, example_num=None):
    file_predictions = []
    for chunk_index, chunk in enumerate(chunks):
        # Process chunk and handle both dict and string types
        if isinstance(chunk, dict) and 'text' in chunk and 'layout' in chunk:
            chunk_content = chunk['text'] + ' ' + chunk['layout']
        elif isinstance(chunk, str):
            chunk_content = chunk
        else:
            raise ValueError(f"Expected a string or dict with 'text' and 'layout' for chunk, but got {type(chunk)}: {chunk}")

        # Generate prompt based on dtype
        prompt = generate_prompt(dtype, prompt_type, chunk_content, examples, template_type, level_type, example_num)
        
        try:
            # Get model output with retry handling
            model_output = run_conversation_with_retry(prompt, MODEL)
            logging.info(f"Raw Model output: {model_output}")

            # Parse model output based on dtype
            if dtype == "reg":
                extracted_info_list = parse_model_output(model_output)
            else:
                logging.info(f"PARSE MODEL OUTPUT: parse_model_output_ad")
                extracted_info_list = parse_model_output_ad(model_output)
            
            logging.info(f"Extracted Info List: {extracted_info_list}")

            # Validate that the extracted information is a list of dictionaries
            if not extracted_info_list or not isinstance(extracted_info_list, list):
                raise ValueError("Failed to parse model output or no information extracted")
                continue

            # Validate that each item in the list is a dictionary
            if not all(isinstance(item, dict) for item in extracted_info_list):
                raise ValueError(f"Expected a list of dictionaries for extracted info, but got: {extracted_info_list}")
            
            # Extend file_predictions with the list of dictionaries
            file_predictions.extend(extracted_info_list)
        
        except RateLimitError:
            logging.error(f"Rate limit error exceeded for chunk {chunk_index + 1}/{len(chunks)}. Skipping this chunk.")
        except Exception as e:
            logging.error(f"An error occurred while processing chunk {chunk_index + 1}/{len(chunks)}: {e}")

    return file_predictions

def process_chunks_token_counts(chunks, prompt_type, examples, template_type, level_type,
                   MODEL, tokenizer, dtype, example_num=None):
    total_token_count = 0  # Store cumulative token count

    for chunk_index, chunk in enumerate(chunks):
        # Process chunk and handle both dict and string types
        if isinstance(chunk, dict) and 'text' in chunk and 'layout' in chunk:
            chunk_content = chunk['text'] + ' ' + chunk['layout']
        elif isinstance(chunk, str):
            chunk_content = chunk
        else:
            raise ValueError(f"Expected a string or dict with 'text' and 'layout' for chunk, but got {type(chunk)}: {chunk}")

        # Generate prompt based on dtype
        prompt = generate_prompt(dtype, prompt_type, chunk_content, examples, template_type, level_type, example_num)

        try:
            # Tokenize the prompt and count tokens
            tokenized_prompt = tokenizer.encode(prompt)
            prompt_token_count = len(tokenized_prompt)

            # Accumulate total token count
            total_token_count += prompt_token_count

            logging.info(f"Chunk {chunk_index + 1}/{len(chunks)}: Token Count = {prompt_token_count}")

        except Exception as e:
            logging.error(f"An error occurred while tokenizing chunk {chunk_index + 1}/{len(chunks)}: {e}")

    return total_token_count  # Return accumulated token count


