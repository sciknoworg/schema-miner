import os
import yaml
import json
import logging
from pathlib import Path

def read_yaml_file(file_path: str, enc: str = 'utf-8'):
    """
    Reads a YAML Configuration file and returns the content in a dictionary format

    :param str file_path: The path to the YAML file
    :param str enc: YAML file encoding
    :return config_dict: The dictionary containing the content of the YAML file. In case of exception, 'None' is returned! 
    """
    # Initialize the logger
    logger = logging.getLogger(__name__)
    try:
        with open(file = file_path, mode = 'r', encoding = enc) as f:
            cfg = yaml.load(f, Loader=yaml.FullLoader)
        return cfg
    except FileNotFoundError:
        logger.debug(f'File NOT Found at path: {file_path}')
    except Exception as e:
        logger.debug(f'Exception occured: {e},\nType: {type(e)}')
    return None

def read_json_file(filepath: str, encoding: str = 'utf-8'):
    """
    Reads the JSON file and return it's content

    :param str file_path: The path to the JSON file
    :param str encoding: The encoder to use for reading the file
    :returns json_dict: The JSON file content
    """
    # Initialize the logger
    logger = logging.getLogger(__name__)
    try:
        with open(filepath, 'r', encoding=encoding) as f:
            data = json.load(f)
        return data
    except json.JSONDecodeError:
        logger.debug('Cannot parse JSON file: {}'.format(filepath))
    except FileNotFoundError:
        logger.debug('File Not Found: {}'.format(filepath))
    except Exception as e:
        logger.debug('Exception occured: {}'.format(e))

def save_json_file(filepath, filename, data, encoding = 'utf-8'):
    """
    Save the JSON Data on a file with the specified encodings

    :param str filepath: The path to the JSON file
    :param str filename: The name of the JSON fle
    :param str encoding: The encoder to use for reading the file
    :returns file_saved: Returns True if the JSON data was saved successfully, False otherwise
    """
    # Initialize the logger
    logger = logging.getLogger(__name__)
    try:
        #Checking if the directory exist, if not create the directory
        os.makedirs(filepath, exist_ok=True)
        filename = '{}/{}'.format(filepath, filename)

        #Writing the JSON data on the file
        with open(filename, 'w', encoding=encoding) as f:
            json.dump(data, f, indent=4)
        return True
    except json.JSONDecodeError:
        logger.debug('Cannot parse JSON file: {}'.format(filepath))
    except Exception as e:
        logger.debug('Exception occured: {}'.format(e))
        return False
    
def read_text_file(file_path: str, enc: str = 'utf-8'):
    """
    Reads a text file and returns the content

    :param str file_path: The path to the file
    :param str enc: file encoding
    :return str: The content of the text file. In case of exception, 'None' is returned! 
    """
    # Initialize the logger
    logger = logging.getLogger(__name__)
    try:
        with open(file = file_path, mode = 'r', encoding = enc) as f:
            data = f.read()
        return data
    except FileNotFoundError:
        logger.debug(f'File NOT Found at path: {file_path}')
    except Exception as e:
        logger.debug(f'Exception occured: {e},\nType: {type(e)}')
    return None

def write_text_file(file_path: str, text: str, encoding: str = 'utf-8'):
    """
    Creates and writes the list of text to a text file

    :param str file_path: The path to save the text file
    :param str text: The text, which has to be saved on the text file
    :returns file_saved: True if the file was saved successfully, otherwise False
    """
    # Initialize the logger
    logger = logging.getLogger(__name__)
    try:
        #Checking if the directory exist, if not create the directory
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, 'w', encoding = encoding) as f:
            f.write(text)
        return True
    except Exception as e:
        logger.debug('Exception occured: {}'.format(e))
        return False
    
def load_text_input(input_val: str | Path) -> str:
    """
    Resolve a text input that may be provided as either a file path or a direct string. If the input corresponds to an existing file path, the file will be read and its contents returned as a string. If the input does not match a valid file path, it is treated as the text itself and returned unchanged.

    :param str | Path input_val: Either a string or `pathlib.Path` object pointing to a text file.
    :returns str: The resolved text content, either loaded from the file or returned as provided.
    """
    if not isinstance(input_val, (str, Path)):
        raise TypeError("The input must be a string or Path object")
    path = Path(input_val)
    text = read_text_file(str(path)) if path.is_file() else input_val
    return text

def load_json_input(input_val: dict | Path) -> dict:
    """
    Resolve a JSON input that may be provided as either a file path or a dictionary. If the input corresponds to an existing file path, the file will be read and its contents returned as a dictionary. If the input does not match a valid file path, it is treated as the dictionary itself and returned unchanged.

    :param dict | Path input_val: Either a dictionary or `pathlib.Path` object pointing to a JSON file.
    :returns dict: The resolved JSON content, either loaded from the file or returned as provided.
    """
    if not isinstance(input_val, (dict, Path)):
        raise TypeError("The input must be a dictionary or Path object")
    json = read_json_file(str(input_val)) if isinstance(input_val, Path) and input_val.is_file() else input_val
    return json