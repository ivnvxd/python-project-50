from typing import Any
import itertools

from gendiff.constants import (
    ADDED,
    REMOVED,
    UNCHANGED,
    UPDATED,
    NESTED,

    TEMPLATE_NESTED,
    TEMPLATE_STYLISH,
)


def make_stylish(diff: list) -> str:
    """
    Render the difference tree in "stylish" format.

    :param diff: Difference tree.
    :return: String of difference visualization in "stylish" format.
    """

    def iter_(data: Any, depth: int = 0) -> str:

        lines = []
        indent = '    ' * depth
        data.sort(key=lambda node: node['key'])

        for node in data:

            if node['type'] == REMOVED:
                lines.append(render_line(
                    node['key'], node['old_value'], '-', depth)
                )

            elif node['type'] == ADDED:
                lines.append(render_line(
                    node['key'], node['new_value'], '+', depth)
                )

            elif node['type'] == UNCHANGED:
                lines.append(render_line(
                    node['key'], node['old_value'], ' ', depth)
                )

            elif node['type'] == UPDATED:
                lines.append(render_line(
                    node['key'], node['old_value'], '-', depth)
                )
                lines.append(render_line(
                    node['key'], node['new_value'], '+', depth)
                )

            elif node['type'] == NESTED:
                lines.append(TEMPLATE_NESTED.format(
                    indent, node['key'], iter_(node['children'],
                                               depth + 1)
                ))

        result = itertools.chain("{", lines, [indent + "}"])

        return '\n'.join(result)

    result = iter_(diff)

    return result


def render_line(key: Any, value: Any, sign: str, depth: int) -> str:
    """
    Render one line of given data in proper format.

    :param key: Name of node to render.
    :param value: Value of current node.
    :param sign: Sign, whether the node was added or removed ('+', '-' etc.)
    :param depth: Indentation value of current line.
    :return: Line of data to add to final render.
    """

    indent = ('    ' * depth)
    lines = []

    if isinstance(value, dict):
        lines.append(TEMPLATE_STYLISH.format(
            indent, sign, key, render_dict(value, depth + 1)))

    else:
        lines.append(TEMPLATE_STYLISH.format(
            indent, sign, key, convert(value)))

    return '\n'.join(lines)


def render_dict(dict_: dict, depth: int) -> str:
    """
    Render dict if it is nested as a value.

    :param dict_: Dictionary to render.
    :param depth: Indentation value of current line.
    :return: Line of data to add to final render.
    """

    lines = []
    indent = '    ' * depth

    for key, value in sorted(dict_.items()):
        lines.append(render_line(key, value, ' ', depth))

    result = itertools.chain("{", lines, [indent + "}"])

    return '\n'.join(result)


def convert(value: Any) -> str:
    """
    Converts input data to unify it while comparing.

    :param value: Value to be converted.
    :return: String in unified format.
    """

    if isinstance(value, bool):
        converted = str(value).lower()
    elif value == '':
        converted = ''
    elif value is None:
        converted = 'null'
    else:
        converted = str(value)

    return converted
