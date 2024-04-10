import json
from typing import Any

CONFIG_FILE_PATH = 'config.json'

import json

def read_config() -> dict:
    """
    Reads the content of the config file and returns it as a dictionary.

    Returns:
    A dictionary containing the contents of the config file. If the config file doesn't exist, an empty dictionary is returned.
    """
    try:
        with open(CONFIG_FILE_PATH, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}  # Return an empty dict if the config file doesn't exist

def write_config_entry(key: str, value: Any) :
    """
    Writes a key-value pair to the config file.

    Parameters:
    - key (str): The key to be written to the config file.
    - value (Any): The corresponding value associated with the key.

    Note:
    This function updates the existing config file, adding or modifying the specified key-value pair.
    """
    config_data = read_config()
    config_data[key] = value
    with open(CONFIG_FILE_PATH, 'w') as file:
        json.dump(config_data, file, indent=4)


def read_config_entry(key: str, default: Any = None) -> dict:
    """
    Reads the config.json file and retrieves the value associated with the specified key.

    Parameters:
    - key (str): The key for which the corresponding value is to be retrieved from the config.json file.
    - default (Any, optional): The default value to return if the specified key is not found. Default is None.

    Returns:
    The value associated with the specified key in the config.json file. If the key is not found, the default value
    provided is returned.
    """
    config_data = read_config()
    print(config_data)
    return config_data.get(key, default)


