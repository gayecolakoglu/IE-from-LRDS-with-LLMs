# data_processing.py

import os
import gzip
import json
import pdfplumber
import logging
import base64
from PIL import Image
import markdown
from bs4 import BeautifulSoup
from pdf2image import convert_from_path
from typing import Dict, List, Union

def categorize_files_by_template(directory):
    # Define the mapping from directory patterns to filename checks
    template_checks = {
        'lv1': 'STL',
        'lv3': 'UTL'
    }

    template_types = ['Amendment', 'Dissemination', 'Short-Form']

    # Initialize categorized files with nested dictionaries
    categorized_files = {
        'STL': {'Amendment': set(), 'Dissemination': set(), 'Short-Form': set()},
        'UTL': {'Amendment': set(), 'Dissemination': set(), 'Short-Form': set()},
    }

    try:
        for filename in os.listdir(directory):
            if filename.endswith(".json"):
                file_path = os.path.join(directory, filename)
                with open(file_path, 'r') as file:
                    data = json.load(file)

                    # Determine level from filename
                    for lv, level_name in template_checks.items():
                        if lv in filename:
                            # Determine template type from filename
                            for template_type in template_types:
                                if template_type in filename:
                                    # Update categorized files with data only from the test key
                                    categorized_files[level_name][template_type].update(data.get('test', []))
                                    break
                            break
                    else:
                        logging.warning(f"Skipping file with unknown level/template type: {filename}")

    except Exception as e:
        logging.error(f"Error categorizing files by template: {e}")

    return categorized_files

def extract_text_from_pdf(pdf_path, dataset_path, use_custom_ocr, transformation_method):
    if use_custom_ocr:
        with pdfplumber.open(pdf_path) as pdf:
            if transformation_method == 'layout-aware':
                ocr_data = {
                    'text': '',
                    'pages': []
                }
                for page_number, page in enumerate(pdf.pages):
                    page_data = {
                        'page_id': page_number,
                        'dimension': {
                            'height': page.height,
                            'width': page.width
                        },
                        'text': page.extract_text(),
                        'lines': [],
                        'paragraphs': [],
                        'blocks': []
                    }
                    for line in page.lines:
                        line_data = {
                            'bbox': line['bbox'],
                            'text': line['text']
                        }
                        page_data['lines'].append(line_data)

                    for paragraph in page.paragraphs:
                        paragraph_data = {
                            'bbox': paragraph['bbox'],
                            'text': paragraph['text']
                        }
                        page_data['paragraphs'].append(paragraph_data)

                    for block in page.blocks:
                        block_data = {
                            'bbox': block['bbox'],
                            'text': block['text']
                        }
                        page_data['blocks'].append(block_data)

                    ocr_data['pages'].append(page_data)

                ocr_data['text'] = ' '.join([page['text'] for page in ocr_data['pages'] if page['text']])
                return ocr_data

            else:
                text = ''
                for page in pdf.pages:
                    text += page.extract_text()
                return {'text': text}

    else:
        _, ocr_texts = load_dataset(dataset_path)
        ocr_text = ocr_texts.get(os.path.basename(pdf_path), {})
        
        if ocr_text:
            if transformation_method == 'layout-aware':
                ocr_data = {
                    'text': ocr_text.get('text', ""),
                    'pages': ocr_text.get('pages', [])
                }
                return ocr_data
            else:
                return {'text': ocr_text.get('text', "")}
        else:
            print("OCR output not found for the PDF in the dataset.")
            return {'text': ""}

def load_dataset(file_path):
    annotations = {}
    ocr_texts = {}
    try:
        with gzip.open(file_path, "rt") as jsonl_file:
            for line in jsonl_file:
                data = json.loads(line)
                filename = data["filename"]
                annotations[filename] = data["annotations"]
                ocr_texts[filename] = data.get("ocr", "")
    except Exception as e:
        logging.error(f"Error loading dataset: {e}")
    return annotations, ocr_texts

def clean_ground_truth_annotations(annotations):
    """
    Clean and correct the structure of ground truth annotations.
    """
    cleaned_annotations = {}

    for filename, file_annotations in annotations.items():
        cleaned_file_annotations = []

        if not isinstance(file_annotations, list):
            print(f"Error: Annotations for file {filename} are not a list.")
            continue

        for annotation in file_annotations:
            if not isinstance(annotation, list) or len(annotation) < 2:
                print(f"Error: Invalid annotation format in file {filename}: {annotation}")
                continue

            entity_name, values = annotation

            # Ensure entity names are strings
            if isinstance(entity_name, list):
                entity_name = [str(name) for name in entity_name]

            # Process values to extract only relevant data
            cleaned_values = []
            if isinstance(values, list):
                for value in values:
                    if isinstance(value, list) and len(value) > 0:
                        # Extract the first element as the actual value (ignoring position info)
                        actual_value = value[0]
                        if isinstance(actual_value, str):
                            cleaned_values.append(actual_value.strip())
                        elif isinstance(actual_value, list) and len(actual_value) > 0:
                            cleaned_values.append(actual_value[0].strip())
                    elif isinstance(value, str):
                        cleaned_values.append(value.strip())

            if cleaned_values:
                cleaned_file_annotations.append([entity_name, cleaned_values])

        cleaned_annotations[filename] = cleaned_file_annotations

    return cleaned_annotations

def structure_ground_truth(annotations, filename):
    """
    Convert the cleaned ground truth annotations to the desired JSON format.
    The output includes both singular attributes and line items grouped in a list.
    """
    structured_data = {
        "advertiser": "",
        "agency": "",
        "contract_num": "",
        "flight_from": "",
        "flight_to": "",
        "gross_amount": "",
        "line_item": [],
        "product": "",
        "property": "",
        "tv_address": ""
    }

    if filename not in annotations:
        print(f"Error: File {filename} not found in annotations.")
        return structured_data

    file_annotations = annotations[filename]

    # Create a mapping from entity name to its corresponding key in the structured data
    singular_keys = {
        "advertiser": "advertiser",
        "agency": "agency",
        "contract_num": "contract_num",
        "flight_from": "flight_from",
        "flight_to": "flight_to",
        "gross_amount": "gross_amount",
        "product": "product",
        "property": "property",
        "tv_address": "tv_address"
    }

    line_item_keys = [
        "channel", "program_desc", "program_end_date", "program_start_date", "sub_amount"
    ]

    for annotation in file_annotations:
        if not isinstance(annotation, list) or len(annotation) < 2:
            print(f"Error: Invalid annotation format for file {filename}: {annotation}")
            continue

        entity_names, values = annotation

        # Handle singular attributes
        if isinstance(entity_names, str) and entity_names in singular_keys:
            if len(values) > 0 and isinstance(values[0], str):
                structured_data[singular_keys[entity_names]] = values[0].strip()

        # Handle line items
        elif isinstance(entity_names, list) and all(name in line_item_keys for name in entity_names):
            # Create a dictionary for the line item
            line_item = {}
            for i, name in enumerate(entity_names):
                if i < len(values):
                    value = values[i]
                    if isinstance(value, str):
                        line_item[name] = value.strip()
                    elif isinstance(value, list) and len(value) > 0:
                        line_item[name] = value[0].strip()
                else:
                    line_item[name] = ""  # Placeholder for missing values

            structured_data["line_item"].append(line_item)

    return structured_data

def process_ground_truth_annotations_ad(filename, cleaned_annotations):
    """
    Process ground truth annotations by cleaning and normalizing them.
    """
    structured_ground_truth = structure_ground_truth(cleaned_annotations, filename)

    return structured_ground_truth

def process_ground_truth_annotations(
    original_filename: str, 
    ground_truth_annotations: Dict[str, List[List[Union[str, List[Union[str, float, List[int]]]]]]]
) -> Dict[str, List[str]]:
    """
    Processes ground truth annotations from a file and returns them in a structured format.

    Args:
        original_filename: The name of the file whose annotations are being processed.
        ground_truth_annotations: A dictionary mapping original_filename to their respective annotations.
                                  Each annotation is a list where:
                                  - The first element is the entity name (str).
                                  - The second element is a list of lists. Each inner list contains:
                                    - A value (str).
                                    - Metadata as a list of numbers or other nested lists.

    Returns:
        A dictionary representing the processed ground truth annotations where:
        - Keys are entity names (str).
        - Values are lists of strings representing the values for each entity, with metadata ignored.
    """
    ground_truth_annotations_for_file = ground_truth_annotations.get(original_filename, [])
    logging.info(f"Processing annotations for file: {original_filename}")

    ground_truth: Dict[str, List[str]] = {}
    for annotation in ground_truth_annotations_for_file:
        if isinstance(annotation, list) and len(annotation) > 1:
            entity = annotation[0]  # Entity name
            values = annotation[1]  # List of lists containing values and metadata

            # Extract the value strings, ignoring metadata
            ground_truth[entity] = [
                value_info[0].strip()  # Strip whitespace or newlines from the value
                for value_info in values
                if isinstance(value_info, list)
                and len(value_info) > 0
                and isinstance(value_info[0], str)
            ]
        else:
            logging.error(f"Annotation format is incorrect for file: {original_filename}")
    return ground_truth

def get_markdown_files_by_template(base_dir, level_type):
    # Define available template types
    template_types = ['Amendment', 'Dissemination', 'Short-Form']

    # Initialize a dictionary to store categorized files
    categorized_files = {template_type: [] for template_type in template_types}

    # Iterate over each template type directory
    for template_type in template_types:
        template_path = os.path.join(base_dir, level_type, template_type)

        # Check if the directory exists
        if not os.path.exists(template_path):
            logging.warning(f"Directory does not exist: {template_path}")
            continue

        # Get all markdown files in the directory
        markdown_files = [os.path.join(template_path, f) for f in os.listdir(template_path) if f.endswith('.md')]
        categorized_files[template_type].extend(markdown_files)

        # Log the number of files found
        logging.info(f"Found {len(markdown_files)} markdown files in {template_path}")

    return {level_type: categorized_files}
    
def extract_text_from_markdown(markdown_content):
    try:
        # Convert markdown content to HTML
        html = markdown.markdown(markdown_content)
        logging.debug(f"Converted HTML: {html[:500]}...")  # Log the first 500 characters of the HTML

        # Use BeautifulSoup to extract text from the HTML
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text()
        
        logging.debug(f"Extracted text from markdown: {text[:500]}...")  # Log the first 500 characters of the extracted text
        return text
    except Exception as e:
        logging.error(f"Failed to extract text from markdown: {e}")
        return ""

def pdf_to_image_paths(pdf_path, temp_pdf_dir):
    try:
        images = convert_from_path(pdf_path)
        image_paths = []
        for i, image in enumerate(images):
            raw_image_path = os.path.join(temp_pdf_dir, f"raw_page_{i + 1}.png")
            image.save(raw_image_path, 'PNG')
            
            # Convert and resize image
            resized_image_path = os.path.join(temp_pdf_dir, f"page_{i + 1}.jpg")
            if convert_and_resize_image(raw_image_path, resized_image_path):
                image_paths.append(resized_image_path)
        
        if not image_paths:
            logging.error(f"No images extracted from PDF: {pdf_path}")
            print(f"No images extracted from PDF: {pdf_path}")
        
        logging.info(f"Converted PDF {pdf_path} to images: {image_paths}")
        print(f"Converted PDF {pdf_path} to images: {image_paths}")
        return image_paths
    except Exception as e:
        logging.error(f"Error converting PDF to images: {e}")
        print(f"Error converting PDF to images: {e}")
        return []

def convert_and_resize_image(image_path, output_path, max_size=(2048, 2048), max_file_size=20*1024*1024):
    try:
        with Image.open(image_path) as img:
            img = img.convert("RGB")  # Ensure image is in RGB format
            img.thumbnail(max_size)   # Resize image to fit within max_size

            quality = 85  # Initial quality for JPEG compression

            # Save the image to the output path with appropriate format and quality
            img.save(output_path, format="JPEG", quality=quality)

            # Check file size and adjust quality if necessary
            while os.path.getsize(output_path) > max_file_size and quality > 10:
                quality -= 5  # Decrease quality incrementally
                img.save(output_path, format="JPEG", quality=quality)
                logging.info(f"Adjusting image quality to {quality} to reduce file size")

        logging.info(f"Converted and resized image saved to {output_path} with final quality {quality}")
        print(f"Converted and resized image saved to {output_path} with final quality {quality}")
        return output_path

    except Exception as e:
        logging.error(f"Error converting and resizing image: {e}")
        print(f"Error converting and resizing image: {e}")
        return None

def encode_image(image_path):
    try:
        with open(image_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
            return encoded_image
    except Exception as e:
        logging.error(f"Error encoding image {image_path}: {e}")
        print(f"Error encoding image {image_path}: {e}")
        return ""
