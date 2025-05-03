import os
import re
import yaml
import json

def read_json_file(filepath: str, encoding: str = 'utf-8'):
    """
    Reads the JSON file and return it's content

    :param str file_path: The path to the JSON file
    :param str encoding: The encoder to use for reading the file
    
    :returns json_dict: The JSON file content
    """
    try:
        with open(filepath, 'r', encoding=encoding) as f:
            data = json.load(f)
        return data
    except json.JSONDecodeError:
        print('Cannot parse JSON file: {}'.format(filepath))
    except FileNotFoundError:
        print('File Not Found: {}'.format(filepath))
    except Exception as e:
        print('Exception Occured: {}'.format(e))

def read_yaml_file(file_path: str, enc: str = 'utf-8'):
    """
    Reads a YAML Configuration file and returns the content in a dictionary format

    :param str file_path: The path to the YAML file
    :param str enc: YAML file encoding
    :return config_dict: The dictionary containing the content of the YAML file. In case of exception, 'None' is returned! 
    """
    try:
        with open(file = file_path, mode = 'r', encoding = enc) as f:
            cfg = yaml.load(f, Loader=yaml.FullLoader)
        return cfg
    except FileNotFoundError:
        print(f'File NOT Found at path: {file_path}')
    except Exception as e:
        print(f'Exception Occured: {e},\nType: {type(e)}')
    return None

def read_text_file(file_path: str, enc: str = 'utf-8'):
    """
    Reads a text file and returns the content

    :param str file_path: The path to the file
    :param str enc: file encoding
    :return str: The content of the text file. In case of exception, 'None' is returned! 
    """
    try:
        with open(file = file_path, mode = 'r', encoding = enc) as f:
            data = f.read()
        return data
    except FileNotFoundError:
        print(f'File NOT Found at path: {file_path}')
    except Exception as e:
        print(f'Exception Occured: {e},\nType: {type(e)}')
    return None

def save_json_file(filepath, filename, data, encoding = 'utf-8'):
    """
    Save the JSON Data on a file with the specified encodings

    :param str filepath: The path to the JSON file
    :param str filename: The name of the JSON fle
    :param str encoding: The encoder to use for reading the file

    :returns file_saved: Returns True if the JSON data was saved successfully, False otherwise
    """
    try:
        #Checking if the directory exist, if not create the directory
        os.makedirs(filepath, exist_ok=True)
        filename = '{}/{}'.format(filepath, filename)

        #Writing the JSON data on the file
        with open(filename, 'w', encoding=encoding) as f:
            json.dump(data, f, indent=4)
        return True
    except json.JSONDecodeError:
        print('Cannot parse JSON file: {}'.format(filepath))
    except Exception as e:
        print('Exception Occured: {}'.format(e))
        return False

def write_text_file(file_path: str, text: str, encoding: str = 'utf-8'):
    """
    Creates and writes the list of text to a text file

    :param str file_path: The path to save the text file
    :param str text: The text, which has to be saved on the text file
    :returns file_saved: True if the file was saved successfully, otherwise False
    """
    try:
        #Checking if the directory exist, if not create the directory
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, 'w', encoding = encoding) as f:
            f.write(text)
        return True
    except Exception as e:
        print('Exception Occured: {}'.format(e))
        return False

def delete_dictionary_keys(dictionary: dict, keys_to_delete: list):
    """
    Deletes a list of keys from the provided dictionary recursively and returns the updated dictionary.

    :param dict dictionary: The dictionary containing the keys to delete
    :param list keys_to_delete: The list of keys to be deleted from the dictionary
    :return dict: The updated dictionary
    """
    #Extracting the keys from the dictionary
    dict_keys = list(dictionary.keys())

    #Iterating over the dictionary keys
    for key in dict_keys:
        #Deleting the key if present in the keys to delete list
        if key in keys_to_delete:
            dictionary.pop(key)
        #Recursively calling the function for nested dictionary
        elif isinstance(dictionary[key], dict):
            delete_dictionary_keys(dictionary[key], keys_to_delete)
    
    #Returning the updated dictionary
    return dictionary

def extract_json_schema(text:str, json_encl_expr: list):
    """
    Extracts the JSON schema from a given text. The JSON schema is enclosed within the start expression and end expression

    :param str text: The text containing the JSON schema
    :param str json_encl_expr: The list of tuples containing start and end expression between which JSON schema is stored.
    :return dict: The extracted JSON schema
    """
    #Intialize schema
    schema = None
    
    #Check if the response only contains the JSON object
    try:
        schema = json.loads(text.strip())
        return schema
    except Exception as e:
        print('The LLM\'s response does not contains only the JSON Schema')
        print('Now, Extracting the JSON Schema enclosed within the start expression and end expression')

    #Trying every start and end expression combination to extract JSON object
    for expr in json_encl_expr:
        #Formatting the regex
        json_extract_pattern = fr"{expr[0]}(.*?){expr[1]}"
        
        #Extracting the JSON schema
        matches = re.findall(json_extract_pattern, text, re.DOTALL)
        if matches:
            try:
                schema = json.loads(''.join(matches))
                break
            except Exception as e:
                print(f'Exception occured while trying {expr} as the start and end expression')
    
    #Returning the extracted schema or if not found: None
    return schema