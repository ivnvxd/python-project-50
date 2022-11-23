#!/usr/bin/env python3

from typing import NoReturn
from gendiff import generate_diff, parse_arguments


def main() -> NoReturn:
    """
    "Gendiff" program entry point.

    Output the result of the generate_diff() function.

    :return: NoReturn
    """
    args = parse_arguments()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
