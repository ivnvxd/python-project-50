import argparse


def parse_arguments() -> argparse.Namespace:
    """
    Parses the data entered into the console to run the program.

    Parameters:
        - first_file (str): First file for comparison.
        - second_file (str): Second file for comparison.
        - format (str): Format for comparison (default: stylish).
    :return: Parsed input values (argparse.Namespace)
    """
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')

    parser.add_argument("first_file")
    parser.add_argument("second_file")

    parser.add_argument(
        '-f', '--format',
        help='set format of output (default: \'stylish\')',
        default='stylish'
    )

    args = parser.parse_args()

    return args
