from gendiff.formatters.render_stylish import make_stylish
from gendiff.formatters.render_plain import make_plain
from gendiff.formatters.render_json import make_json

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
        return make_stylish(diff)
    elif format == PLAIN:
        return make_plain(diff)
    elif format == JSON:
        return make_json(diff)
