import argparse

from gendiff.constants import (
    STYLISH,
    PLAIN,
    JSON
)


def parse_arguments():
    """
    Parses the data entered into the console to run the program.

    Parameters:
        - first_file (str): First file for comparison.
        - second_file (str): Second file for comparison.
        - format (str): Format for comparison (default: stylish).
    :return: Parsed input values (argparse arguments)
    """
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')

    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)

    parser.add_argument(
        '-f', '--format',
        type=str,
        help="set format of output (default: 'stylish')",
        choices=[STYLISH, PLAIN, JSON],
        default=STYLISH
    )

    args = parser.parse_args()

    return args
