# postprocessing.py

import re
import unicodedata
from dateutil import parser
import json
import logging
from typing import Dict, Union, Tuple, List, Optional


def map_schema_keys(reconciled_predictions: dict, defined_schema: dict, synonym_dict: dict = None) -> dict:
    """
    Map reconciled_predictions keys to defined schema using exact, partial, and synonym-based matching.
    
    Args:
    - reconciled_predictions (dict): Keys from the model output.
    - defined_schema (dict): Defined schema with keys.
    - synonym_dict (dict): Optional predefined dictionary of synonyms for schema keys.

    Returns:
    - dict: Mapping of output keys to schema keys.
    """
    synonym_dict = {
        "file_date": ["file date", "date", "record date", "filing date"],
        "foreign_principle_name": ["foreign principle", "foreign principal name", "principal"],
        "registrant_name": ["registrant", "registration name", "entity name"],
        "registration_num": ["registration number", "reg number", "reg id"],
        "signer_name": ["signer", "signatory", "authorized representative"],
        "signer_title": ["title", "designation", "role", "position"],
    }

    synonym_dict_reverse = {}
    for key, value in synonym_dict.items():
        for item in value:
            synonym_dict_reverse[item] = key

    predicted_mapped = {}
    for pred_key, pred_value in reconciled_predictions.items():
        if pred_key in synonym_dict_reverse:
            predicted_mapped[synonym_dict_reverse[pred_key]] = pred_value
        else:
            predicted_mapped[pred_key] = pred_value

    return predicted_mapped

def clean_data(reconciled_predictions: Dict[str, Union[str, Tuple[str, ...], List[str]]]
) -> Dict[str, Union[str, Tuple[str, ...], List[str]]]:
    """
    Cleans and normalizes reconciled predictions.

    Args:
        reconciled_predictions: A dictionary where keys are prediction fields and values are strings, tuples of strings, or lists of strings.

    Returns:
        A dictionary with cleaned and normalized predictions.
    """
    cleaned_data: Dict[str, Union[str, Tuple[str, ...], List[str]]] = {}

    for pred_key, pred_value in reconciled_predictions.items():
        # If the value is a tuple, process each element individually
        if isinstance(pred_value, tuple):
            pred_value = tuple(normalize_pred_value(val) for val in pred_value)
            
            # Apply additional normalization for specific fields
            if pred_key == "file_date":
                pred_value = tuple(normalize_date(val) for val in pred_value)
            elif pred_key in ["foreign_principle_name", "registrant_name", "signer_name"]:
                pred_value = tuple(normalize_name(val) for val in pred_value)
            elif pred_key == "registration_num":
                pred_value = tuple(re.sub(r'\D', '', val) for val in pred_value)

        # If the value is a list, process each element individually
        elif isinstance(pred_value, list):
            pred_value = [normalize_pred_value(val) for val in pred_value]
            
            # Apply additional normalization for specific fields
            if pred_key == "file_date":
                pred_value = [normalize_date(val) for val in pred_value]
            elif pred_key in ["foreign_principle_name", "registrant_name", "signer_name"]:
                pred_value = [normalize_name(val) for val in pred_value]
            elif pred_key == "registration_num":
                pred_value = [re.sub(r'\D', '', val) for val in pred_value]

        # If the value is a single string, process it normally
        else:
            pred_value = normalize_pred_value(pred_value)

            # Apply additional normalization for specific fields
            if pred_key == "file_date":
                pred_value = normalize_date(pred_value)
            elif pred_key in ["foreign_principle_name", "registrant_name", "signer_name"]:
                pred_value = normalize_name(pred_value)
            elif pred_key == "registration_num":
                pred_value = re.sub(r'\D', '', pred_value)  # Remove non-digit characters

        cleaned_data[pred_key] = pred_value

    return cleaned_data


def normalize_pred_value(pred_value: Union[str, tuple[str, ...]]) -> Union[str, tuple[str, ...]]:
    """
    Basic text normalization to prepare values for comparison.
    
    Args:
        pred_value: A string or a tuple of strings to be normalized.
    
    Returns:
        The normalized string or tuple of strings.
    """
    if isinstance(pred_value, tuple):
        return tuple(
            unicodedata.normalize('NFKD', val).encode('ascii', 'ignore').decode('utf-8').strip().lower()
            for val in pred_value
        )
    else:
        pred_value = unicodedata.normalize('NFKD', pred_value)  # Normalize accents and special characters
        pred_value = pred_value.encode('ascii', 'ignore').decode('utf-8')  # Remove non-ASCII characters
        pred_value = re.sub(r'\s+', ' ', pred_value).strip().lower()  # Normalize whitespace and lowercase
        return pred_value

def normalize_date(pred_value: str) -> str:
    """
    Normalize dates to the format YYYY-MM-DD.

    Args:
        pred_value: The date string to normalize.

    Returns:
        The normalized date in YYYY-MM-DD format, or the original string if parsing fails.
    """
    try:
        parsed_date = parser.parse(re.sub(r'[\n+\s]+day of', '', pred_value, flags=re.IGNORECASE))
        return parsed_date.strftime('%Y-%m-%d')
    except ValueError:
        return pred_value  # Return original if parsing fails


def normalize_name(pred_value: Union[str, tuple[str, ...]]) -> Union[str, tuple[str, ...]]:
    """
    Normalize names by capitalizing each word.

    Args:
        pred_value: A string or a tuple of strings to normalize.

    Returns:
        The normalized string or tuple of strings.
    """
    if isinstance(pred_value, tuple):
        return tuple(' '.join(word.capitalize() for word in re.sub(r'\s+', ' ', name).strip().split()) for name in pred_value)
    else:
        return ' '.join(word.capitalize() for word in re.sub(r'\s+', ' ', pred_value).strip().split())

def parse_model_output(model_output):
    if not model_output.strip():
        return []

    json_str = clean_model_output(model_output)
    
    try:
        output_json = json.loads(json_str)

        # Ensure we have a list of dictionaries
        if isinstance(output_json, dict):
            output_json = [output_json]
        if not isinstance(output_json, list) or not all(isinstance(i, dict) for i in output_json):
            logging.error(f"Parsed output is not a list of dictionaries: {output_json}")
            raise ValueError("Parsed output should be a list of dictionaries.")
        
        # extracted_info_list = []

        # # Correct the extraction logic
        # for item in output_json:
        #     extracted_info = {
        #         "file_date": item.get("file_date") or None,
        #         "foreign_principle_name": item.get("foreign_principle_name") or None,
        #         "registrant_name": item.get("registrant_name") or None,
        #         "registration_num": item.get("registration_num") or None,
        #         "signer_name": item.get("signer_name") or None,
        #         "signer_title": item.get("signer_title") or None
        #     }
        #    extracted_info_list.append(extracted_info)

        extracted_info_list = [item for item in output_json]
        
        return extracted_info_list
    
    except json.JSONDecodeError as e:
        logging.error(f"Error parsing JSON from model output: {e}")
        logging.error(f"Model output: {repr(model_output)}")
        return []
    except Exception as e:
        logging.error(f"An error occurred while parsing model output: {e}")
        return []

def parse_model_output_ad(model_output):
    """
    Parse the model output and extract relevant information.
    """
    if not model_output.strip():
        logging.warning("Model output is empty or whitespace.")
        return []

    # Clean the model output
    json_str = clean_model_output(model_output)

    try:
        # Parse the cleaned JSON string
        output_json = json.loads(json_str)

        # Ensure output_json is a list of dictionaries
        if isinstance(output_json, dict):
            output_json = [output_json]

        if not isinstance(output_json, list) or not all(isinstance(i, dict) for i in output_json):
            logging.error(f"Parsed output is not a list of dictionaries: {output_json}")
            raise ValueError("Parsed output should be a list of dictionaries.")

        extracted_info_list = []

        # Extract information from each item
        for item in output_json:
            extracted_info = {
                "advertiser": item.get("advertiser", ""),
                "agency": item.get("agency", ""),
                "contract_num": item.get("contract_num", ""),
                "flight_from": item.get("flight_from", ""),
                "flight_to": item.get("flight_to", ""),
                "gross_amount": item.get("gross_amount", ""),
                "line_item": item.get("line_item", []),
                "product": item.get("product", ""),
                "property": item.get("property", ""),
                "tv_address": item.get("tv_address", "")
            }

            # Ensure line_items are properly formatted
            if isinstance(extracted_info["line_item"], list):
                formatted_line_items = []
                for line_item in extracted_info["line_item"]:
                    if isinstance(line_item, dict):  # Ensure line_item is a dictionary
                        formatted_line_item = {
                            "channel": line_item.get("channel", ""),
                            "program_desc": line_item.get("program_desc", ""),
                            "program_start_date": line_item.get("program_start_date", ""),
                            "program_end_date": line_item.get("program_end_date", ""),
                            "sub_amount": line_item.get("sub_amount", "")
                        }
                        formatted_line_items.append(formatted_line_item)
                extracted_info["line_item"] = formatted_line_items

            extracted_info_list.append(extracted_info)
        return extracted_info_list

    except json.JSONDecodeError:
        logging.error("Error parsing JSON from model output:", exc_info=True)
        logging.debug(f"Model output that caused error: {repr(model_output)}")
        return []
    except Exception as e:
        logging.error("An error occurred while parsing model output:", exc_info=True)
        return []

def clean_model_output(model_output):
    """
    Clean model output to extract JSON data.
    """
    try:
        # Remove single-line comments (// comment)
        model_output = re.sub(r'//.*$', '', model_output, flags=re.MULTILINE)
        # Remove multi-line comments (/* comment */)
        model_output = re.sub(r'/\*.*?\*/', '', model_output, flags=re.DOTALL)
        # Extract the JSON part from the model_output
        json_start = model_output.find("{")
        json_end = model_output.rfind("}") + 1
        json_str = model_output[json_start:json_end]
        return json_str
    except Exception as e:
        raise ValueError("Error cleaning model output:", exc_info=True)
        return ""


def reconcile_predictions(predictions: List[Dict[str, Union[str, List[str]]]]) -> Dict[str, Union[str, Tuple[str, ...]]]:
    """
    Reconciles a list of predictions into a single prediction by performing deduplication and majority voting.

    Args:
        predictions: A list of dictionaries where each dictionary represents a prediction. Values can be strings or lists of strings.

    Returns:
        A dictionary representing the reconciled prediction, with values as strings or tuples of strings.
    """
    print(f"\nRAW PRED: {predictions}")

    
    # Deduplicate predictions based on their content
    try:
        flat_predictions = []
        for pred in predictions:
            flat_pred = {}
            for key, value in pred.items():
                # Convert lists to tuples for hashable handling or keep as-is
                if isinstance(value, list):
                    flat_pred[key] = tuple(value)  # Convert to tuple for hashable keys
                else:
                    flat_pred[key] = value
            flat_predictions.append(flat_pred)
    
    except TypeError as e:
        logging.error(f"Error during deduplication: {e}. Flat predictions: {predictions}")
        raise

    print("\nFLAT PRED: ", flat_predictions)
    
    reconciled_predictions = {}
    for entity in flat_predictions[0].keys():
        values = [pred.get(entity, None) for pred in flat_predictions if pred.get(entity) and pred.get(entity) != "[]"]
        
        # Flatten and deduplicate values
        unique_values = set()
        for value in values:
            if isinstance(value, dict):  # Handle dictionaries
                continue 
            if isinstance(value, tuple):  # Handle flattened lists (tuples)
                unique_values.update(value)  # Unpack and add each element
            else:  # Handle single values
                unique_values.add(value)

        unique_values = {v for v in unique_values if v and v != "[]"}

        # Convert the set to a tuple if there are multiple unique items
        unique_values_list = sorted(unique_values)  # Sort for consistency
        if unique_values_list:
            # If there's more than one unique value, keep them as a tuple
            if len(unique_values_list) > 1:
                reconciled_predictions[entity] = tuple(unique_values_list)
            else:
                # Single value as a string
                reconciled_predictions[entity] = unique_values_list[0]
        else:
            # If no non-empty values exist, assign an empty string
            reconciled_predictions[entity] = ''

    print("\nReconciled PRED: ", reconciled_predictions)
    logging.debug(f"Reconciled predictions: {reconciled_predictions}")
    return reconciled_predictions
    
def reconcile_predictions_ad(flat_predictions):
    # Create a set to store unique, hashable items
    unique_predictions = set()

    for pred in flat_predictions:
        # Convert the prediction to a hashable form
        try:
            hashable_pred = make_hashable(pred)
            # Add to the set
            unique_predictions.add(hashable_pred)
        except TypeError as e:
            logging.error(f"Error adding prediction to set: {pred} - {e}")

    # Convert the unique, hashable items back to dictionaries
    reconciled_predictions = [convert_to_dict(item) for item in unique_predictions]

    return reconciled_predictions

def make_hashable(item):
    """
    Recursively convert a dictionary to a hashable format.
    """
    if isinstance(item, dict):
        # Convert dictionary to frozenset of its items, with line_item handled separately
        return frozenset((key, make_hashable(value)) for key, value in item.items())
    elif isinstance(item, list):
        # Convert list to a tuple of hashable items
        return tuple(make_hashable(sub_item) for sub_item in item)
    return item  # Return the item itself if it is already hashable

def convert_to_dict(hashable_item):
    """
    Convert a hashable frozenset back to a dictionary.
    """
    if isinstance(hashable_item, frozenset):
        # Convert frozenset back to a dictionary
        return {key: convert_to_dict(value) for key, value in hashable_item}
    elif isinstance(hashable_item, tuple):
        # Convert tuple back to a list
        return [convert_to_dict(sub_item) for sub_item in hashable_item]
    return hashable_item  # Return the item itself if it is already in a simple form