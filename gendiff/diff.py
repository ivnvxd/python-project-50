from gendiff.file_handler import open_file


def generate_diff(file1_path: str, file2_path: str, format: str = '') -> str:

    file1 = open_file(file1_path)
    file2 = open_file(file2_path)

    diff = get_diff(file1, file2)

    return render_diff(diff)


def get_diff(file1: dict, file2: dict) -> list:
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


def render_diff(diff: list) -> str:
    difference = '{\n'

    for line in diff:
        difference += f'  {line}\n'

    difference += '}'

    return difference
