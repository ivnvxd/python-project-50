import json
import yaml
import os


def generate_diff(file_path1, file_path2, format=''):

    name1, ext1 = os.path.splitext(file_path1)
    name2, ext2 = os.path.splitext(file_path2)

    if ext1 == ext2:

        if ext1 == '.json':
            file1 = json.load(open(file_path1))
            file2 = json.load(open(file_path2))

        elif ext1 == '.yml' or ext1 == '.yaml':
            file1 = yaml.safe_load(open(file_path1))
            file2 = yaml.safe_load(open(file_path2))

    diff = get_diff(file1, file2)

    return render_diff(diff)


def get_diff(file1, file2):
    keys = sorted(file1.keys() | file2.keys())
    diff = []

    for key in keys:

        if key in file1 and key not in file2:
            if isinstance(file1[key], bool):
                file1[key] = str(file1[key]).lower()
            diff.append(f'- {key}: {file1[key]}')

        elif key not in file1 and key in file2:
            if isinstance(file2[key], bool):
                file2[key] = str(file2[key]).lower()
            diff.append(f'+ {key}: {file2[key]}')

        elif file1[key] == file2[key]:
            if isinstance(file1[key], bool):
                file1[key] = str(file1[key]).lower()
            diff.append(f'  {key}: {file1[key]}')

        else:
            if isinstance(file1[key], bool):
                file1[key] = str(file1[key]).lower()
            diff.append(f'- {key}: {file1[key]}')
            if isinstance(file2[key], bool):
                file2[key] = str(file2[key]).lower()
            diff.append(f'+ {key}: {file2[key]}')

    return diff


def render_diff(diff):
    difference = '{\n'

    for line in diff:
        difference += f'  {line}\n'

    difference += '}'

    return difference
