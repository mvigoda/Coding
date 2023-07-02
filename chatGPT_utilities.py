import os
import openai
import webbrowser
import json
import csv
import datetime
from datetime import datetime
from docx import Document

def read_file(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()
        return contents
    
def write_to_file(file_name,patient_note,response):
    file = open(file_name + '.txt' ,'w') 
    now = datetime.now()

    formatted_date = now.strftime("%a %b %d at %H:%M")
    print(f'{formatted_date}')
    file.write('Created on: ' + formatted_date + '\n'*2 )
    
    file.write(patient_note + '\n'*2 )
    file.write(response + '\n'*2 )
    print(f'{file_name} was created in {os.getcwd()}')
    file.close() 
    return









def extract_letters(string):
    pattern = r' (\w+):'
    matches = re.findall(pattern, string)
    return matches

def setup_OpenAI_API():
    """
    In the event that 'chatGPT_key.txt' is in the same directory, do not go up one dir
    """

    
    starting_directory = os.getcwd()
    print(f'starting_directory {starting_directory}')
    chatGPT_key_file = 'chatGPT_key.txt'
    if chatGPT_key_file not in os.listdir():
        print(f'going to directory above')
        os.chdir('..')
    print(f'Directory:{os.getcwd()}')
    dir_above = os.getcwd()
    chatGPT_key_file = 'chatGPT_key.txt'
    assert  chatGPT_key_file in os.listdir(), 'Missing ChatGPT key'
    with open(chatGPT_key_file, 'r') as file:
        data = file.read()
        # print(data)
    openai.api_key  = data
    if os.getcwd() != starting_directory:
        os.chdir(starting_directory)
    assert os.getcwd() == starting_directory , 'We should be in starting directory'
    return data





def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"] 


def get_completion_from_messages(messages, 
                                 model="gpt-3.5-turbo", 
                                 temperature=0, 
                                 max_tokens=500):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens,
    )
    return response.choices[0].message["content"]

def get_completion_from_messages_FULL(messages, 
                                 model="gpt-3.5-turbo", 
                                 temperature=0, 
                                 max_tokens=500):
    """
    # get_completion_from_messages_FULL  
    Returns **response** which is a *openai.openai_object.OpenAIObject*  :
    - id
    - object
    - created
    - model
    - usage
    - choices
    """
    
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens,
    )
    return response



def print_token_usage(response_details,cost_per_unit = 0.002, number_tokens_per_unit = 1000):
    try:
        # print(response.choices[0].message["content"])
        print('\033[91m\033[1m' + '\n\nToken Usage:'+ '\033[0m')
        print(f'Cost to run query is based on token usage, which is $0.002 / 1K tokens')
        print(f'Completion tokens: {response_details.usage["completion_tokens"]:10,.0f}')
        print(f'Prompt tokens    : {response_details.usage["prompt_tokens"]:10,.0f}')
        print(f'Total tokens     : {response_details.usage["total_tokens"]:10,.0f}')
    except:
        print(f'The response does not contain any token usage data')
        print(f'This is because we used "get_completion_from_messages"')
        print(f'If you want token usage data you must use "get_completion_from_messages_FULL"')
    cost_of_tokens = cost_per_unit * (response_details.usage["total_tokens"]/number_tokens_per_unit)
    cost_of_query = round(cost_of_tokens,3)
    return cost_of_query




# def print_token_usage(response_details,cost_per_unit = 0.002, number_tokens_per_unit = 1000):
#     print(f'Cost to run query is based on token usage, which is $0.002 / 1K tokens')
#     try:
#         # print(response.choices[0].message["content"])
#         print(f'\n\nToken Usage:\n\n')
#         print(f'completion_tokens: {response_details.usage["completion_tokens"]}')
#         print(f'prompt_tokens    : {response_details.usage["prompt_tokens"]}')
#         print(f'total_tokens     : {response_details.usage["total_tokens"]}')
#     except:
#         print(f'The response does not contain any token usage data')
#         print(f'This is because we used "get_completion_from_messages"')
#         print(f'If you want token usage data you must use "get_completion_from_messages_FULL"')
#     cost_of_tokens = cost_per_unit * (response_details.usage["total_tokens"]/number_tokens_per_unit)
#     cost_of_query = round(cost_of_tokens,3)
#     return cost_of_query

def token_usage(response_details,cost_per_unit = 0.002, number_tokens_per_unit = 1000):
    try:
        cost_of_tokens = cost_per_unit * (response_details.usage["total_tokens"]/number_tokens_per_unit)
        cost_of_query = round(cost_of_tokens,3)
        return cost_of_query
    except:
        print(f'The response does not contain any token usage data, as you most likely used "get_completion_from_messages"')
        print(f'If you want token usage data you must use "get_completion_from_messages_FULL"')
        return None




def json_to_dict(json_str):
    try:
        json_dict = json.loads(json_str)
        return json_dict
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {str(e)}")
        return {}


def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None




def openai_object_to_dict(obj):
    if isinstance(obj, dict):
        return {key: openai_object_to_dict(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [openai_object_to_dict(item) for item in obj]
    elif hasattr(obj, "__dict__"):
        return openai_object_to_dict(vars(obj))
    else:
        return obj
    




def categorize_primary_secondary_categories(delimiter,
                                            system_message,
                                            list_messages):
    
    for message in list_messages:
        print(f"User's message: {message}:\n")
        user_message = f"""\n\n\
        {message}"""
        messages =  [  
        {'role':'system', 
         'content': system_message},    
        {'role':'user', 
         'content': f"{delimiter}{user_message}{delimiter}"},  
        ] 
        response = get_completion_from_messages(messages)
        response = json_to_dict(response)
        # print(response)
        for k,v in response.items():
            print(f'{k.title():10}: {v.title()}')
        print('\n'*2 ) 
    return

def generate_markdown(data):
    markdown = "| "
    markdown += " | ".join(data[0])
    markdown += " |\n"
    markdown += "| " + " | ".join(["---"] * len(data[0])) + " |\n"
    for row in data[1:]:
        markdown += "| "
        markdown += " | ".join(row)
        markdown += " |\n"
    return markdown

def CSV_to_DICT(file_name):
    # csv_file = "4_specialties_multiple_locations.csv"  # Replace with the path to your CSV file
    assert '.csv' in file_name, f'{csv_file} is NOT a CSV file'
    data = {}

    # Read the CSV file
    with open(file_name, mode="r") as file:
        reader = csv.reader(file)
        headers = next(reader)  # Read the header row

        for row in reader:
            primary_key = row[0]  # Primary key from the first column
            secondary_key = row[1]  # Secondary key from the second column
            values = row[2:]  # Values from the remaining columns

            if primary_key in data:
                # Primary key already exists, make the secondary key a nested dictionary
                if secondary_key not in data[primary_key]:
                    data[primary_key][secondary_key] = values
            else:
                # Primary key doesn't exist, create a new entry
                data[primary_key] = {secondary_key: values}

    # Print the resulting dictionary
    # print(data)
    return data

def create_dictionary_doctors_locations(csv_file):
    dictionary = {}
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row if it exists
        sorted_data = sorted(reader, key=lambda row: row[0])  # Sort the data by clinic name
        for row in sorted_data:
            clinic_name = row[0]
            doctor_name = row[1]
            availability = row[2]
            if clinic_name not in dictionary:
                dictionary[clinic_name] = {}
            dictionary[clinic_name][doctor_name] = availability
    return dictionary

# Usage example
# file_doctors_locations = 'Doctors_at_Clinic_Locations.csv'
# doctors_dict = create_dictionary_doctors_locations(file_doctors_locations)
# pp_json(doctors_dict)

# # json_doctors_locations_avail = json.dumps(doctors_dict)
# # print(f'data is of {type(json_doctors_locations_avail)}')
# # pp_json(json_doctors_locations_avail)
# print(f'We are using "clinics_dict" and "doctors_dict"')

def read_string_to_list(input_string): # Read Python string into Python list of dictionaries
    if input_string is None:
        return None

    try:
        input_string = input_string.replace("'", "\"")  # Replace single quotes with double quotes for valid JSON
        data = json.loads(input_string)
        return data
    except json.JSONDecodeError:
        print("Error: Invalid JSON string")
        return None   

# Retrieve detailed product information for the relevant products and categories¶
def generate_output_string(data_list):
    output_string = ""

    if data_list is None:
        return output_string

    for data in data_list:
        try:
            if "products" in data:
                products_list = data["products"]
                for product_name in products_list:
                    product = get_product_by_name(product_name)
                    if product:
                        output_string += json.dumps(product, indent=4) + "\n"
                    else:
                        print(f"Error: Product '{product_name}' not found")
            elif "category" in data:
                category_name = data["category"]
                category_products = get_products_by_category(category_name)
                for product in category_products:
                    output_string += json.dumps(product, indent=4) + "\n"
            else:
                print("Error: Invalid object format")
        except Exception as e:
            print(f"Error: {e}")

    return output_string

def create_dictionary_of_lists(file_path):
    dictionary = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            key = line.split(':')[0]
            value = line.split(':')[1]
            # print(key,'-----',value)
            if key in dictionary:
                dictionary[key].append(value)
            else:
                dictionary[key] = [value]
    return dictionary

def create_dictionary_doctors_locations(csv_file):
    dictionary = {}
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row if it exists
        sorted_data = sorted(reader, key=lambda row: row[0])  # Sort the data by clinic name
        for row in sorted_data:
            clinic_name = row[0]
            doctor_name = row[1]
            availability = row[2]
            if clinic_name not in dictionary:
                dictionary[clinic_name] = {}
            dictionary[clinic_name][doctor_name] = availability
    return dictionary



def convert_string_to_json(string):
    try:
        json_obj = json.loads(string)
        return json_obj
    except json.JSONDecodeError as e:
        print(f"Error converting string to JSON: {e}")
        return None


def convert_dict_to_json(dictionary):
    try:
        json_str = json.dumps(dictionary)
        return json_str
    except TypeError as e:
        print(f"Error converting dictionary to JSON: {e}")
        return None
    
def replace_with_bold_red(string, substring):
    """
    : Replace substring with BOLD RED in the string
    """
    string = string.replace(substring,'\033[91m'+\
                                     '\033[1m' + '\n\n' + substring + '\033[0m') 
    return string

def write_to_file(file_name,patient_note,response):
    file = open(file_name + '.txt' ,'w') 
    now = datetime.now()
    formatted_date = now.strftime("%a %b %d at %H:%M") #print(f'{formatted_date}')
    file.write('Created on: ' + formatted_date + '\n'*2 )
    file.write(patient_note + '\n'*2 )
    file.write(response + '\n'*2 ) #print(f'{file_name} was created in {os.getcwd()}')
    file.close() 
    return


def capitalize_all_letters(string):
    capitalized_string = ""
    for char in string:
        if char.isalpha():
            capitalized_string += char.upper()
        else:
            capitalized_string += char
    return capitalized_string


def color_code_clinic_note(string,
                           list_substrings,
                          color):
    """
    : Input   : pt_note, which is a text string 
                list_substrings, which are substrings
    : Output  :
    """
    printing_colors = { 'Red' : '\033[91;1m',
                   'Green' : '\033[92;1m',
                    'Brown' : '\033[38;5;94;1m',
                    'Blue' :  '\033[38;5;18;1m'  ,
                    'Orange' : '\033[38;5;208;1m',
                    'Black': '\033[255;0;0;1m',
                    'Magenta' : '\033[38;5;90m',
                    'Purple' : '\033[38;5;54m'}


    
   
    assert color in printing_colors.keys(), \
    color +  ' is NOT a recognized color for "color_code_clinic_note"'

    string_for_display = string
    for substr in list_substrings:
        # patient_note_for_display = patient_note_for_display.replace(substr,
        #                                                             '\033[91m\033[1m' + substr + '\033[0m')
        string_for_display = string_for_display.replace(substr,
                                  printing_colors[color] + substr +  '\033[0m' )
    return string_for_display

def highlight_text(text):
    YELLOW_BACKGROUND = '\033[43m'
    RESET_FORMATTING = '\033[0m'
    return YELLOW_BACKGROUND + text + RESET_FORMATTING

def convert_response_STR_to_DICT(response):
    clean_string = response.replace('\n', '') # Remove unnecessary characters ('\n') from the string
    data_dict = json.loads(clean_string)  # Convert the cleaned string to a dictionary
    return data_dict

