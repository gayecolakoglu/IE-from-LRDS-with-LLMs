# arrange_conf.py

from config import MODEL_gpt_3, MODEL_gpt_4, MODEL_llama, folder_path_reg, folder_path_reg_md, dataset_path_reg, folder_path_ad_md, folder_path_ad, dataset_path_ad
import os
import json
import logging

def get_log_directory(directory, model):
    if directory == 'vrdu2/registration-form/few_shot-splits/' and model == MODEL_gpt_3:
        return 'gpt4_Markdown_gpt3_outputs/reg/'
    elif directory == 'vrdu2/registration-form/few_shot-splits/' and model == MODEL_gpt_4:
        return 'gpt4_Markdown_gpt4_outputs/reg/'
    elif directory == 'vrdu2/registration-form/few_shot-splits/'  and model == MODEL_llama:
        return 'gpt4_Markdown_Llama3_outputs/reg/'
    elif directory == 'vrdu2/ad-buy-form/few_shot-splits/'  and model == MODEL_gpt_3:
        return 'gpt4_Markdown_gpt3_outputs/ad/'
    elif directory == 'vrdu2/ad-buy-form/few_shot-splits/'  and model == MODEL_gpt_4:
        return 'gpt4_Markdown_gpt4_outputs/ad/'
    elif directory == 'vrdu2/ad-buy-form/few_shot-splits/'  and model == MODEL_llama:
        return 'gpt4_Markdown_Llama3_outputs/ad/'
    else:
        raise ValueError("Directory not recognized for logging configuration")

def get_log_directory_md(directory, model):
    if directory == 'vrdu2/registration-form/few_shot-splits/' and model == MODEL_gpt_4:
        return 'gpt4_Markdown_outputs/reg/'
    elif directory == 'vrdu2/ad-buy-form/few_shot-splits/' and model == MODEL_gpt_4:
        return 'gpt4_Markdown_outputs/ad/'
    else:
        raise ValueError("Directory not recognized for logging configuration")

def get_log_directory_img(directory, model):
    if directory == 'vrdu2/registration-form/few_shot-splits/' and model == MODEL_gpt_4:
        return 'gpt4_outputs_Image/reg/'
    elif directory == 'vrdu2/ad-buy-form/few_shot-splits/' and model == MODEL_gpt_4:
        return 'gpt4_outputs_Image/ad/'
    else:
        raise ValueError("Directory not recognized for logging configuration")

def get_output_directory(directory, model):
    if directory == 'vrdu2/registration-form/few_shot-splits/' and model == MODEL_gpt_3:
        return 'gpt4_Markdown_gpt3_outputs/reg/'
    elif directory == 'vrdu2/registration-form/few_shot-splits/' and model == MODEL_gpt_4:
        return 'gpt4_Markdown_gpt4_outputs/reg/'
    elif directory == 'vrdu2/registration-form/few_shot-splits/'  and model == MODEL_llama:
        return 'gpt4_Markdown_Llama3_outputs/reg/'
    elif directory == 'vrdu2/ad-buy-form/few_shot-splits/'  and model == MODEL_gpt_3:
        return 'gpt4_Markdown_gpt3_outputs/ad/'
    elif directory == 'vrdu2/ad-buy-form/few_shot-splits/'  and model == MODEL_gpt_4:
        return 'gpt4_Markdown_gpt4_outputs/ad/'
    elif directory == 'vrdu2/ad-buy-form/few_shot-splits/'  and model == MODEL_llama:
        return 'gpt4_Markdown_Llama3_outputs/ad/'
    else:
        raise ValueError("Directory not recognized for logging configuration")

def get_output_directory_md(directory, model):
    if directory == 'vrdu2/registration-form/few_shot-splits/' and model == MODEL_gpt_4:
        return 'gpt4_Markdown_outputs/reg/'
    elif directory == 'vrdu2/ad-buy-form/few_shot-splits/' and model == MODEL_gpt_4:
        return 'gpt4_Markdown_outputs/ad/'
    else:
        raise ValueError("Directory not recognized for logging configuration")

def get_output_directory_img(directory, model):
    if directory == 'vrdu2/registration-form/few_shot-splits/' and model == MODEL_gpt_4:
        return 'gpt4_outputs_Image/reg/'
    elif directory == 'vrdu2/ad-buy-form/few_shot-splits/' and model == MODEL_gpt_4:
        return 'gpt4_outputs_Image/ad/'
    else:
        raise ValueError("Directory not recognized for logging configuration")


def get_data_paths_md(directory):
    folder_path = ""
    dataset_path = ""
    dtype = ""
    
    if directory == 'vrdu2/registration-form/few_shot-splits/':
        folder_path = folder_path_reg_md
        dataset_path = dataset_path_reg
        dtype = 'reg'
        return folder_path, dataset_path, dtype
    elif directory == 'vrdu2/ad-buy-form/few_shot-splits/':
        folder_path = folder_path_ad_md
        dataset_path = dataset_path_ad
        dtype = 'ad'
        return folder_path, dataset_path, dtype
    else:
        print("Directory not recognized")
        return "", "", ""
    

def get_data_paths(directory):
    folder_path = ""
    dataset_path = ""
    dtype = ""
    
    if directory == 'vrdu2/registration-form/few_shot-splits/':
        folder_path = folder_path_reg
        dataset_path = dataset_path_reg
        dtype = 'reg'
        return folder_path, dataset_path, dtype
    elif directory == 'vrdu2/ad-buy-form/few_shot-splits/':
        folder_path = folder_path_ad
        dataset_path = dataset_path_ad
        dtype = 'ad'
        return folder_path, dataset_path, dtype
    else:
        print("Directory not recognized")
        return "", "", ""

