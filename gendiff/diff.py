from gendiff.file_handler import open_file
from gendiff.find_diff import get_diff
from gendiff.formatters.render import render

from gendiff.constants import (
    STYLISH
)


def generate_diff(file1: str, file2: str, format: str = STYLISH) -> str:
    """
    Opens two files to be compared, calculates difference between them
    and returns the difference in chosen format.

    :param file1: Path to the first file.
    :param file2: Path to the second file.
    :param format: Format of the output (stylish/plain)
    :return: Visualized difference tree in chosen format.
    """
    file1 = open_file(file1)
    file2 = open_file(file2)

    diff = get_diff(file1, file2)

    return render(diff, format)
