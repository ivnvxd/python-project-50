import json
import yaml


def open_file(file_path):
    """
    Open file and return a stream.

    :param file_path: Path of the file to open.
    :return: Stream data from the opened file.
    """

    with open(file_path) as file:
        return load(file_path, file)


def load(path: str, file) -> dict:
    """
    Loads data based on the passed extension.

    :param path: Path of file to load.
    :param file: Stream data from the opened file.
    :returns: data (dict): Data from opened file im Python dictionary object.
    """

    if path.endswith('.yaml') or path.endswith('.yml'):
        return yaml.safe_load(file)
    elif path.endswith('.json'):
        return json.load(file)
