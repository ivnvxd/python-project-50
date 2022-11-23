from gendiff.formatters.stylish import render_stylish
from gendiff.formatters.plain import render_plain

from gendiff.constants import (
    STYLISH,
    PLAIN
)


def render(diff: list, format: str) -> str:
    """
    Calls rendering function based on selected format.

    :param diff: Difference tree.
    :param format: Chosen format (stylish/plain).
    :return: Rendering function.
    """

    if format == STYLISH:
        return render_stylish(diff)
    elif format == PLAIN:
        return render_plain(diff)
