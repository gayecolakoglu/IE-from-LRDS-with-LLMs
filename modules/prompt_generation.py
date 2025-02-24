# prompt_generation.py

import json

def generate_no_schema_prompt(text, template_type='Amendment'):
    # Define task descriptions for different template types
    task_descriptions = {
        'Amendment': '''
        Extract the following entities as JSON: file_date, foreign_principle_name, registrant_name, registration_num, signer_name, signer_title. 
        If you cannot find the value of a key, just write "" or [] instead of the corresponding value.
        Do not include any additional text, explanations, comments, or formatting. Ensure that all keys and values are properly escaped and do not include special characters that might break the JSON format.
        ''',
        'Dissemination': '''
        Extract the following entities as JSON: file_date, foreign_principle_name, registrant_name, registration_num, dissemination_channel, dissemination_date. 
        If you cannot find the value of a key, just write "" or [] instead of the corresponding value.
        Do not include any additional text, explanations, comments, or formatting. Ensure that all keys and values are properly escaped and do not include special characters that might break the JSON format.
        ''',
        'Short-Form': '''
        Extract the following entities as JSON: file_date, foreign_principle_name, registrant_name, short_form_type, contact_name, contact_email. 
        If you cannot find the value of a key, just write "" or [] instead of the corresponding value.
        Do not include any additional text, explanations, comments, or formatting. Ensure that all keys and values are properly escaped and do not include special characters that might break the JSON format.
        '''
    }

    task_description = task_descriptions.get(template_type, task_descriptions[template_type])
    return f"<Document>\n{text}\n<Task>\n{task_description}\n</Task>"

def generate_no_schema_prompt_ad(text):
    task_description = (
        '''
        Extract the following entities as JSON: advertiser, agency, contract_num, flight_from, flight_to, gross_amount, line_item[{channel, program_desc, program_end_date, program_start_date, sub_amount}], product, property, tv_address. 
        If you cannot find the value of a key, just write "" or [] instead of the corresponding value.
        Do not include any additional text, explanations, comments, or formatting. Ensure that all keys and values are properly escaped and do not include special characters that might break the JSON format.
        '''
    )
    return f"<Document>\n{text}\n<Task>\n{task_description}\n</Task>"

def generate_few_shot_prompt(text, examples, template_type='Amendment', level_type='STL'):
    prompt = ""
    if examples:
        prompt += "### Examples ###\n"
        for example in examples:
            prompt += f"<Document>\n{example['text']}\n<Entities>\n{json.dumps(example['entities'], indent=2)}\n\n"
    
    task_descriptions = {
        'Amendment': '''
        Extract the following entities as JSON: {"file_date": "", "foreign_principle_name": "", "registrant_name": "", "registration_num": "", "signer_name": "", "signer_title": ""}. 
        If you cannot find the value of a key, just write "" or [] instead of the corresponding value.
        Do not include any additional text, explanations, comments, or formatting. Ensure that all keys and values are properly escaped and do not include special characters that might break the JSON format.
        ''',
        'Dissemination': '''
        Extract the following entities as JSON: {"file_date": "", "foreign_principle_name": "", "registrant_name": "", "registration_num": "", "dissemination_channel": "", "dissemination_date": ""}. 
        If you cannot find the value of a key, just write "" or [] instead of the corresponding value.
        Do not include any additional text, explanations, comments, or formatting. Ensure that all keys and values are properly escaped and do not include special characters that might break the JSON format.
        ''',
        'Short-Form': '''
        Extract the following entities as JSON: {"file_date": "", "foreign_principle_name": "", "registrant_name": "", "short_form_type": "", "contact_name": "", "contact_email": ""}. 
        If you cannot find the value of a key, just write "" or [] instead of the corresponding value.
        Do not include any additional text, explanations, comments, or formatting. Ensure that all keys and values are properly escaped and do not include special characters that might break the JSON format.
        '''
    }
    task_description = task_descriptions.get(template_type, task_descriptions[template_type])
    
    # Add additional instructions based on the level type
    if level_type == 'UTL':
        task_description += " This document format may be different from any seen before."

    prompt += f"### New Document ###\n<Document>\n{text}\n<Task>\n{task_description}\n</Task>"
    return prompt

def generate_few_shot_prompt_ad(text, examples, template_type='STL'):
    prompt = ""
    if examples:
        prompt += "### Examples ###\n"
        for example in examples:
            prompt += f"<Document>\n{example['text']}\n<Entities>\n{json.dumps(example['entities'], indent=2)}\n\n"
    
    task_description = (
        ''''
        Extract the following entities as JSON: "entities": {"advertiser": "","agency": "","contract_num": "","flight_from": "", "flight_to": "", "gross_amount": "", "line_item": [ { "channel": "", "program_desc": "", "program_end_date": "", "program_start_date": "", "sub_amount": "" } ], "product": "", "property": "", "tv_address": "" }. 
        If you cannot find the value of a key, just write "" or [] instead of the corresponding value.
        Do not include any additional text, explanations, comments, or formatting. Ensure that all keys and values are properly escaped and do not include special characters that might break the JSON format. 
        '''
    )
    if template_type == 'MTL':
        task_description += " Ensure that you account for possible variations in document format."
    elif template_type == 'UTL':
        task_description += " This document format may be different from any seen before."

    prompt += f"### New Document ###\n<Document>\n{text}\n<Task>\n{task_description}\n</Task>"
    return prompt

def generate_chain_of_thought_prompt(text, examples, template_type='Amendment', level_type='STL'):
    prompt = ""
    if examples:
        prompt += "### Examples with Reasoning ###\n"
        for example in examples:
            prompt += f"<Document>\n{example['text']}\n<Entities>\n{json.dumps(example['entities'], indent=2)}\n<Reasoning>\n{generate_reasoning(example['text'], example['entities'])}\n</Reasoning>\n\n"

    task_descriptions = {
        'Amendment': '''
        Extract the following entities as JSON: {"file_date": "", "foreign_principle_name": "", "registrant_name": "", "registration_num": "", "signer_name": "", "signer_title": ""}. 
        If you cannot find the value of a key, just write "" or [] instead of the corresponding value.
        Do not include any additional text, explanations, comments, or formatting. Ensure that all keys and values are properly escaped and do not include special characters that might break the JSON format. 
        ''',
        'Dissemination': '''
        Extract the following entities as JSON: {"file_date": "", "foreign_principle_name": "", "registrant_name": "", "registration_num": "", "dissemination_channel": "", "dissemination_date": ""}. 
        If you cannot find the value of a key, just write "" or [] instead of the corresponding value.
        Do not include any additional text, explanations, comments, or formatting. Ensure that all keys and values are properly escaped and do not include special characters that might break the JSON format. 
        ''',
        'Short-Form': '''
        Extract the following entities as JSON: {"file_date": "", "foreign_principle_name": "", "registrant_name": "", "short_form_type": "", "contact_name": "", "contact_email": ""}. 
        If you cannot find the value of a key, just write "" or [] instead of the corresponding value.
        Do not include any additional text, explanations, comments, or formatting. Ensure that all keys and values are properly escaped and do not include special characters that might break the JSON format. 
        '''
    }

    task_description = task_descriptions.get(template_type, task_descriptions[template_type])
    
    # Add additional instructions based on the level type
    if level_type == 'UTL':
        task_description += " This document format may be different from any seen before."

    prompt += f"### New Document with Reasoning ###\n<Document>\n{text}\n<Task>\n{task_description}\n</Task>\n<Reasoning>\n{generate_reasoning(text, {'file_date': '', 'foreign_principle_name': '', 'registrant_name': '', 'registration_num': '', 'signer_name': '', 'signer_title': ''})}\n</Reasoning>"
    return prompt

def generate_chain_of_thought_prompt_ad(text, examples, template_type='STL'):
    prompt = ""
    if examples:
        prompt += "### Examples with Reasoning ###\n"
        for example in examples:
            prompt += f"<Document>\n{example['text']}\n<Entities>\n{json.dumps(example['entities'], indent=2)}\n<Reasoning>\n{generate_reasoning(example['text'], example['entities'])}\n</Reasoning>\n\n"

    task_description = (
        '''
        Extract the following entities as JSON: "entities": {"advertiser": "","agency": "","contract_num": "","flight_from": "", "flight_to": "", "gross_amount": "", "line_item": [{"channel": "", "program_desc": "", "program_end_date": "", "program_start_date": "", "sub_amount": ""}], "product": "", "property": "", "tv_address": ""}. 
        If you cannot find the value of a key, just write "" or [] instead of the corresponding value.
        Do not include any additional text, explanations, comments, or formatting. Ensure that all keys and values are properly escaped and do not include special characters that might break the JSON format. 
        '''
    )
    if template_type == 'MTL':
        task_description += " Ensure that you account for possible variations in document format."
    elif template_type == 'UTL':
        task_description += " This document format may be different from any seen before."

    prompt += (
        f"### New Document with Reasoning ###\n<Document>\n{text}\n<Task>\n{task_description}\n</Task>\n<Reasoning>\n"
        f"{generate_reasoning(text, {'advertiser': '', 'agency': '', 'contract_num': '', 'flight_from': '', 'flight_to': '', 'gross_amount': '', 'line_item': [{'channel': '', 'program_desc': '', 'program_end_date': '', 'program_start_date': '', 'sub_amount': ''}], 'product': '', 'property': '', 'tv_address': ''})}\n</Reasoning>"
    )
    return prompt


def generate_reasoning(document_text, entities):
    reasoning = "To extract the entities, follow these steps:\n"
    reasoning += "1. Identify relevant sections.\n"
    reasoning += "2. Match sections with entity fields.\n"
    reasoning += "3. Validate values against known formats.\n"
    reasoning += "4. Compile values into JSON format.\n"
    for entity, value in entities.items():
        reasoning += f"- {entity}: {value}\n"
    return reasoning

def generate_prompt(dtype, prompt_type, text, examples=None, template_type='Amendment', level_type='STL', example_num=None):
    if prompt_type == 'no_schema':
        if dtype == "reg":
            return generate_no_schema_prompt(text, template_type)
        else:
            return generate_no_schema_prompt_ad(text)
    elif prompt_type == 'few_shot':
        if examples is None and example_num != 0:
            raise ValueError("Examples are required for few-shot prompting.")

        if dtype == "reg":
            return generate_few_shot_prompt(text, examples or [], template_type, level_type)
        else:
            return generate_few_shot_prompt_ad(text, examples or [], template_type)
    elif prompt_type == 'chain_of_thought':
        if examples is None and example_num != 0:
            raise ValueError("Examples are required for chain of thought prompting.")
        if dtype == "reg":
            return generate_chain_of_thought_prompt(text, examples or [], template_type, level_type)
        else:
            return generate_chain_of_thought_prompt_ad(text, examples or [], template_type)
        
    else:
        raise ValueError("Unknown prompt type.")

def prompt_token_length_function(prompt):
    if isinstance(prompt, str):
        return len(prompt.split())  # Simplified example; replace with actual tokenization
    else:
        logging.error(f"Expected a string for prompt, but got {type(prompt)}: {prompt}")
        return 0
