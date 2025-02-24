# evaluation.py

import os
import pandas as pd
from collections import defaultdict
import re
from fuzzywuzzy import fuzz # use Levenhstein Distance
from typing import Dict, Union, Tuple, List, Optional, Any
from modules.postprocessing import clean_data, map_schema_keys
from config import defined_schema, comparison_methods

def compare_exact(pred_value: Optional[Union[str, tuple[str, ...]]], gt_value: Optional[Union[str, List[str]]]) -> bool:
    """
    Compare predicted and ground truth values using strict exact matching.

    Args:
        pred_value: The predicted value, which can be a string or a tuple of strings.
        gt_value: The ground truth value, which can be a string or a list of strings.

    Returns:
        True if the predicted value matches the ground truth exactly, False otherwise.
    """
    if isinstance(pred_value, tuple):
        pred_value = list(pred_value)
    else:
        pred_value = [pred_value]

    if isinstance(gt_value, str):
        gt_value = [gt_value]

    return sorted(pred_value) == sorted(gt_value)

def compare_substring(pred_value: Optional[Union[str, tuple[str, ...]]], gt_value: Optional[Union[str, List[str]]]) -> bool:
    """
    Compare predicted and ground truth values to ensure all ground truth values are contained in predictions.

    Args:
        pred_value: The predicted value, which can be a string or a tuple of strings.
        gt_value: The ground truth value, which can be a string or a list of strings.

    Returns:
        True if all ground truth values are substrings of the predicted values, False otherwise.
    """
    if isinstance(pred_value, tuple):
        pred_value = list(pred_value)
    else:
        pred_value = [pred_value]

    if isinstance(gt_value, str):
        gt_value = [gt_value]

    return all(any(gt in pred for pred in pred_value) for gt in gt_value)

def compare_fuzzy(
    pred_value: Optional[Union[str, tuple[str, ...]]], 
    gt_value: Optional[Union[str, List[str]]], 
    threshold: float = 0.8
) -> bool:
    """
    Compare predicted and ground truth values using fuzzy matching.

    Args:
        pred_value: The predicted value, which can be a string or a tuple of strings.
        gt_value: The ground truth value, which can be a string or a list of strings.
        threshold: The similarity threshold for fuzzy matching, between 0 and 1.

    Returns:
        True if all ground truth values have at least one fuzzy match in predictions above the threshold, False otherwise.
    """
    if isinstance(pred_value, tuple):
        pred_value = list(pred_value)
    else:
        pred_value = [pred_value]

    if isinstance(gt_value, str):
        gt_value = [gt_value]

    return all(
        any(fuzz.ratio(gt, pred) / 100 >= threshold for pred in pred_value)
        for gt in gt_value
    )

def compare_values(
    pred_value: Union[str, tuple], 
    gt_value: Union[str, tuple], 
    method: str, 
    threshold: float = 0.8
) -> bool:
    """
    Compare predicted and ground truth values using a specified method.

    Args:
        pred_value: The predicted value, which can be a string or a tuple of strings.
        gt_value: The ground truth value, which can be a string or a tuple of strings.
        method: The comparison method to use ('exact', 'substring', 'fuzzy').
        threshold: The threshold for fuzzy matching (default is 0.9).

    Returns:
        A boolean indicating whether the comparison meets the criteria of the method.
    """
    if method == "exact":
        return compare_exact(pred_value, gt_value)
    elif method == "substring":
        return compare_substring(pred_value, gt_value)
    elif method == "fuzzy":
        return compare_fuzzy(pred_value, gt_value, threshold)
    else:
        raise ValueError(f"Unsupported comparison method: {method}")

def evaluate_response_with_metrics(
    reconciled_predictions: Dict[str, Union[str, Tuple[str, ...]]],
    ground_truth: Dict[str, Union[str, List[str]]]
) -> Dict[str, Union[Dict[str, Union[str, float]], float]]:
    """
    Evaluate and calculate metrics using multiple comparison methods.

    Args:
        reconciled_predictions: Predicted values mapped to schema keys.
        ground_truth: Ground truth values mapped to schema keys.
        defined_schema: A dictionary mapping schema keys to their descriptions.

    Returns:
        A dictionary containing precision, recall, and F1 scores for initial, mapped, and cleaned predictions
        across different comparison methods.
    """
    pp_experiments = []
    predicted_mapped: Dict[str, Union[str, Tuple[str, ...]]] = map_schema_keys(reconciled_predictions, defined_schema)
    cleaned_data: Dict[str, Union[str, Tuple[str, ...]]] = clean_data(reconciled_predictions)
    cleaned_gt: Dict[str, Union[str, Tuple[str, ...]]] = clean_data(ground_truth)  # Clean the ground truth data


    for method, params in comparison_methods.items():
        pp_experiments_w_methods = []
        threshold = params.get("threshold", 0.8)

        for schema_key in defined_schema.keys():
            initial_pred: Union[str, Tuple[str, ...]] = reconciled_predictions.get(schema_key, "")
            mapped_pred: Union[str, Tuple[str, ...]] = predicted_mapped.get(schema_key, "")
            cleaned_pred: Union[str, Tuple[str, ...]] = cleaned_data.get(schema_key, "")
            ground_truth_value: Union[str, List[str]] = ground_truth.get(schema_key, "")
            cleaned_gt_value: Union[str, Tuple[str, ...]] = cleaned_gt.get(schema_key, "")  # Cleaned GT value


            pp_experiments_w_methods.append({
                "schema_key": schema_key,
                "initial_pred": initial_pred,
                "mapped_pred": mapped_pred,
                "cleaned_pred": cleaned_pred,
                "ground_truth_value": ground_truth_value,
                "cleaned_gt_value": cleaned_gt_value,
                "comparison_method": method,
            })
        pp_experiments.extend(pp_experiments_w_methods)

    # Calculate metrics for each method
    comparison_metrics: Dict[str, Union[Dict[str, Union[str, float]], float]] = {}
    for method in comparison_methods:
        method_comparison_results = [r for r in pp_experiments if r["comparison_method"] == method]

        initial_pred = {r["schema_key"]: r["initial_pred"] for r in method_comparison_results}
        mapped_pred = {r["schema_key"]: r["mapped_pred"] for r in method_comparison_results}
        cleaned_pred = {r["schema_key"]: r["cleaned_pred"] for r in method_comparison_results}
        ground_truth_value = {r["schema_key"]: r["ground_truth_value"] for r in method_comparison_results}
        cleaned_gt_value = {r["schema_key"]: r["cleaned_gt_value"] for r in method_comparison_results}

        print(f"\ninitial_pred: {initial_pred}")
        print(f"\nmapped_pred: {mapped_pred}")
        print(f"\ncleaned_pred: {cleaned_pred} ")
        print(f"\nground_truth_value: {ground_truth_value} ")
        print(f"\cleaned_gt_value: {cleaned_gt_value} ")
        
        initial_pred_metrics = calculate_schema_metrics(ground_truth_value, initial_pred, comparison_method=method)
        mapped_pred_metrics = calculate_schema_metrics(ground_truth_value, mapped_pred, comparison_method=method)
        cleaned_pred_metrics = calculate_schema_metrics(cleaned_gt_value, cleaned_pred, comparison_method=method)

        # Add metrics to a dictionary for appending later
        method_key = method.replace(" ", "_")  # Clean up method name for keys
        comparison_metrics.update({
            "mapped_pred": mapped_pred,
            "cleaned_pred": cleaned_pred,
            "cleaned_gt": cleaned_gt_value,
            f"precision_initial_{method_key}": initial_pred_metrics["overall"]["precision"],
            f"precision_mapped_{method_key}": mapped_pred_metrics["overall"]["precision"],
            f"precision_cleaned_{method_key}": cleaned_pred_metrics["overall"]["precision"],
            f"recall_initial_{method_key}": initial_pred_metrics["overall"]["recall"],
            f"recall_mapped_{method_key}": mapped_pred_metrics["overall"]["recall"],
            f"recall_cleaned_{method_key}": cleaned_pred_metrics["overall"]["recall"],
            f"f1_initial_{method_key}": initial_pred_metrics["overall"]["f1"],
            f"f1_mapped_{method_key}": mapped_pred_metrics["overall"]["f1"],
            f"f1_cleaned_{method_key}": cleaned_pred_metrics["overall"]["f1"],
            f"match_results_initial_{method_key}": initial_pred_metrics["overall"]["match_results"],
            f"match_results_mapped_{method_key}": mapped_pred_metrics["overall"]["match_results"],
            f"match_results_cleaned_{method_key}": cleaned_pred_metrics["overall"]["match_results"]
        })

    return comparison_metrics

def calculate_schema_metrics(
    ground_truth: Dict[str, Union[str, Tuple[str], List[str]]],
    predictions: Dict[str, Union[str, Tuple[str], List[str]]],
    comparison_method: str,
    threshold: float = 0.8
) -> Dict[str, Dict[str, Union[float, int]]]:
    """
    Calculate schema-level metrics based on a specific comparison method.

    Args:
        ground_truth: A dictionary where keys are schema keys and values are ground truth values (strings, tuples, or lists).
        predictions: A dictionary where keys are schema keys and values are predicted values (strings, tuples, or lists).
        comparison_method: The comparison method (e.g., "exact", "substring", "fuzzy").
        threshold: A float value for fuzzy matching threshold (used only in comparison methods requiring it).

    Returns:
        A dictionary with metrics for each schema key and overall metrics.
    """
    if not isinstance(ground_truth, dict) or not isinstance(predictions, dict):
        raise ValueError("Both ground_truth and predictions must be dictionaries.")

    schema_metrics = defaultdict(lambda: {"tp": 0, "fp": 0, "fn": 0})
    schema_match_results = {}

    # Compare predictions to ground truth for each schema key
    for gt_key, gt_value in ground_truth.items():
        if gt_key in defined_schema.keys() and gt_value not in [None, ""]:
            pred_value = predictions.get(gt_key, None)
            if pred_value in [None, ""]:  # Key missing in predictions
                schema_metrics[gt_key]["fn"] += 1
                schema_match_results[gt_key] = 0
            else:
                match = compare_values(pred_value, gt_value, comparison_method, threshold)
                print(f"\nComparison result for pred_value: {pred_value} and gt_value: {gt_value} is => {match}")
                if match:
                    schema_metrics[gt_key]["tp"] += 1
                    schema_match_results[gt_key] = 1
                else:
                    schema_metrics[gt_key]["fp"] += 1
                    schema_match_results[gt_key] = 0

    print("\n SCHEMA METRIC: ", schema_metrics)

    # Handle extra keys in predictions (keys in predictions but not in ground truth)
    for pred_key, pred_value in predictions.keys() - defined_schema.keys():
        if pred_key not in schema_metrics:
            schema_metrics[pred_key] = {"tp": 0, "fp": 0, "fn": 0}
        schema_metrics[pred_key]["fp"] += 1
        schema_match_results[pred_key] = 0
        
    # Compute precision, recall, and F1-score for each schema key
    metrics: Dict[str, Dict[str, Union[float, int]]] = {}
    for key, counts in schema_metrics.items():
        tp = counts["tp"]
        fp = counts["fp"]
        fn = counts["fn"]
        precision = tp / (tp + fp) if tp + fp > 0 else 0
        recall = tp / (tp + fn) if tp + fn > 0 else 0
        f1 = 2 * precision * recall / (precision + recall) if precision + recall > 0 else 0

        metrics[key] = {"precision": precision, "recall": recall, "f1": f1, "tp": tp, "fp": fp, "fn": fn}

    # Compute overall metrics
    total_tp = sum(counts["tp"] for counts in schema_metrics.values())
    total_fp = sum(counts["fp"] for counts in schema_metrics.values())
    total_fn = sum(counts["fn"] for counts in schema_metrics.values())

    overall_precision = total_tp / (total_tp + total_fp) if total_tp + total_fp > 0 else 0
    overall_recall = total_tp / (total_tp + total_fn) if total_tp + total_fn > 0 else 0
    overall_f1 = 2 * overall_precision * overall_recall / (overall_precision + overall_recall) if overall_precision + overall_recall > 0 else 0

    metrics["overall"] = {"precision": overall_precision, "recall": overall_recall, "f1": overall_f1, "match_results": schema_match_results}

    return metrics