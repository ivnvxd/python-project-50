from gendiff.file_handler import open_file
from gendiff.find_diff import get_diff_tree
from gendiff.formatters.stylish import render_stylish


def generate_diff(file1_path: str, file2_path: str, format: str) -> str:
    """

    :param file1_path:
    :param file2_path:
    :param format:
    :return:
    """
    file1 = open_file(file1_path)
    file2 = open_file(file2_path)

    diff = get_diff_tree(file1, file2)

    return render_stylish(diff)
