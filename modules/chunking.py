# chunking.py

from modules.prompt_generation import generate_prompt, prompt_token_length_function
from modules.batch_processing import *
import logging
import os

def get_chunk_size(chunk_size_category, prompt_type, num_examples):
    # Define the maximum token limit based on the chunk size category
    if chunk_size_category == 'max':
        max_token_limit = 4096
    elif chunk_size_category == 'medium':
        max_token_limit = 2048
    elif chunk_size_category == 'small':
        max_token_limit = 1024
    else:
        raise ValueError("Invalid chunk size category. Choose from 'max', 'medium', or 'small'.")

    # Calculate base token length based on chosen parameters
    base_token_length = calculate_base_token_length(prompt_type, num_examples)

    # Estimate the chunk size
    buffer = 100  # Define a buffer to avoid exceeding the token limit
    average_tokens_per_word = 1.3  # Average tokens per word for English text
    chunk_size = estimate_chunk_size(max_token_limit, base_token_length, buffer, average_tokens_per_word)

    return chunk_size

def calculate_base_token_length(prompt_type, num_examples):
    base_length = 100  

    if prompt_type == "no_schema":
        base_length += 50
    elif prompt_type == "few_shot":
        base_length += 150 * num_examples  
    elif prompt_type == "template_based":
        base_length += 200  

    return base_length

def estimate_chunk_size(max_token_limit, base_token_length, buffer, average_tokens_per_word=1.3):
    available_tokens = max_token_limit - base_token_length - buffer
    chunk_size_in_words = int(available_tokens / average_tokens_per_word)
    return chunk_size_in_words

def generate_chunk(chunking_method, extracted_data, chunk_size=None, overlap=None, document=None):
    if isinstance(extracted_data, dict):
        extracted_text = extracted_data.get('text', "")
        layout_info = extracted_data.get('pages', [])
        if not isinstance(extracted_text, str):
            logging.error(f"Expected a string for extracted_text, but got {type(extracted_text)} in extracted_data: {extracted_data}")
            return [], 0
    elif isinstance(extracted_data, str):
        extracted_text = extracted_data
        layout_info = None
    else:
        logging.error(f"Expected a string or dictionary for extracted_data, but got {type(extracted_data)}: {extracted_data}")
        return [], 0

    if chunking_method == 'fixed':
        chunks = fixed_length_chunking(extracted_text, chunk_size, layout_info)
        prompt_token_size = sum(prompt_token_length_function(chunk['text'] + ' ' + chunk['layout']) for chunk in chunks)
    elif chunking_method == 'overlapping':
        chunks = overlapping_chunks(extracted_text, chunk_size, overlap)
        prompt_token_size = sum(prompt_token_length_function(chunk) for chunk in chunks)
    elif chunking_method == 'lmdx':
        if document is None:
            logging.error("Document must be provided for lmdx chunking method")
            return [], 0
        chunks = lmdx_chunking(document, chunk_size)
        prompt_token_size = sum(prompt_token_length_function(chunk) for chunk in chunks)
    else:
        raise ValueError("Unknown chunking method.")
    
    logging.info(f"Generated {len(chunks)} chunks with total prompt token size {prompt_token_size}")
    return chunks, prompt_token_size

def fixed_length_chunking(text, chunk_size, layout_info=None, buckets=100):
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0
    document_width = layout_info[0]['dimension']['width'] if layout_info else 1
    document_height = layout_info[0]['dimension']['height'] if layout_info else 1

    def format_segment_text_with_coordinates(segment, width, height, buckets):
        bbox = segment['bbox']
        normalized_coords = normalize_bbox(bbox, width, height)
        quantized_coords = [quantize(coord, buckets) for coord in normalized_coords]
        coordinates = f"{quantized_coords[0]}|{quantized_coords[1]}"
        return f"{segment['text']} {coordinates}segment"

    logging.info(f"Text length: {len(text)}, Chunk size: {chunk_size}")

    for word in words:
        current_chunk.append(word)
        current_length += 1

        if current_length >= chunk_size:
            chunk_text = ' '.join(current_chunk)
            chunk_segments = []

            if layout_info:
                for page in layout_info:
                    for item in page['lines']:
                        if item['text'] in chunk_text:
                            formatted_segment = format_segment_text_with_coordinates(item, document_width, document_height, buckets)
                            chunk_segments.append(formatted_segment)

            chunks.append({
                'text': chunk_text,
                'layout': ' '.join(chunk_segments)
            })
            current_chunk = []
            current_length = 0

    if current_chunk:
        chunk_text = ' '.join(current_chunk)
        chunk_segments = []

        if layout_info:
            for page in layout_info:
                for item in page['lines']:
                    if item['text'] in chunk_text:
                        formatted_segment = format_segment_text_with_coordinates(item, document_width, document_height, buckets)
                        chunk_segments.append(formatted_segment)

        chunks.append({
            'text': chunk_text,
            'layout': ' '.join(chunk_segments)
        })
        logging.info(f"Generated chunk: {chunk_text[:50]}... with length {len(chunk_text)}")

    logging.info(f"Generated {len(chunks)} chunks with total text length {sum(len(chunk['text']) for chunk in chunks)}")
    return chunks

def overlapping_chunks(text, chunk_size, overlap):
    if not isinstance(text, str):
        logging.error(f"Expected a string for text, but got {type(text)}: {text}")
        return []
    
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunks.append(' '.join(words[i:i + chunk_size]))
        i += chunk_size - overlap
    return chunks

def lmdx_chunking(document, chunk_size):
    chunks = []

    for page in document.pages:
        segments = page.segments
        current_chunk = []
        current_chunk_length = 0

        for segment in segments:
            segment_text = segment.text
            segment_length = prompt_token_length_function(segment_text)

            if current_chunk_length + segment_length > chunk_size:
                chunks.append(' '.join(current_chunk))
                current_chunk = [segment_text]
                current_chunk_length = segment_length
            else:
                current_chunk.append(segment_text)
                current_chunk_length += segment_length

        if current_chunk:
            chunks.append(' '.join(current_chunk))

    return chunks

def normalize_bbox(bbox, width, height):
    xmin, ymin, xmax, ymax = bbox
    xcenter = (xmin + xmax) / 2
    ycenter = (ymin + ymax) / 2
    return [
        xcenter / width,
        ycenter / height
    ]

def quantize(value, buckets):
    return int(np.clip(value * buckets, 0, buckets - 1))


