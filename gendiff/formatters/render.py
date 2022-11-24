from gendiff.formatters.render_stylish import render_stylish
from gendiff.formatters.render_plain import render_plain
from gendiff.formatters.render_json import render_json

from gendiff.constants import (
    STYLISH,
    PLAIN,
    JSON
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
    elif format == JSON:
        return render_json(diff)
