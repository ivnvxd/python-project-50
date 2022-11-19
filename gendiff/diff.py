import json


def generate_diff(file_path1, file_path2):

    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))

    diff = get_diff(file1, file2)

    return render_diff(diff)


def get_diff(file1, file2):
    keys = sorted(file1.keys() | file2.keys())
    diff = []

    for key in keys:

        if key in file1 and key not in file2:
            diff.append(f'- {key}: {file1[key]}')

        elif key not in file1 and key in file2:
            diff.append(f'+ {key}: {file2[key]}')

        elif file1[key] == file2[key]:
            diff.append(f'  {key}: {file1[key]}')

        else:
            diff.append(f'- {key}: {file1[key]}')
            diff.append(f'+ {key}: {file2[key]}')

    return diff


def render_diff(diff):
    difference = '{\n'

    for line in diff:
        difference += f'  {line}\n'

    difference += '}'

    return difference
