import json
import yaml


def open_file(file_path: str) -> dict:
    """
    Open file and load it to a dict.

    :param file_path: Path of the file to open.
    :return: data (dict): Data from opened file im Python dictionary object.
    """

    with open(file_path, 'r') as file:
        return load(file_path, file)


def load(path: str, file) -> dict:
    """
    Loads data based on the passed extension.

    :param path: Path of file to load.
    :param file: TextIO data from the opened file
    :returns: data (dict): Data from opened file im Python dictionary object.
    """

    if path.endswith('.yaml') or path.endswith('.yml'):
        return yaml.safe_load(file)
    elif path.endswith('.json'):
        return json.load(file)
