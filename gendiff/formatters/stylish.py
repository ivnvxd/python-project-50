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
    TEMPLATE_EMPTY
)


def render_stylish(diff: list) -> str:
    """

    :param diff:
    :return:
    """

    def iter_(data: Any, depth: int = 0) -> str:

        lines = []
        indent = '    ' * depth

        for node in data:

            if node['type'] == REMOVED:
                lines.append(render_line(
                    node['key'], node['old_value'], '-', depth))

            elif node['type'] == ADDED:
                lines.append(render_line(
                    node['key'], node['new_value'], '+', depth))

            elif node['type'] == UNCHANGED:
                lines.append(render_line(
                    node['key'], node['old_value'], ' ', depth))

            elif node['type'] == UPDATED:
                lines.append(render_line(
                    node['key'], node['old_value'], '-', depth))
                lines.append(render_line(
                    node['key'], node['new_value'], '+', depth))

            elif node['type'] == NESTED:
                lines.append(TEMPLATE_NESTED.format(
                    indent, node['key'], iter_(node['children'],
                                               depth + 1)))

        result = itertools.chain("{", lines, [indent + "}"])

        return '\n'.join(result)

    result = iter_(diff)

    return result


def render_line(key: Any, value: Any, sign: str, depth: int) -> str:
    """

    :param key:
    :param value:
    :param sign:
    :param depth:
    :return:
    """

    indent = ('    ' * depth)
    lines = []

    if isinstance(value, dict):
        lines.append(TEMPLATE_STYLISH.format(
            indent, sign, key, render_dict(value, depth + 1)))

    elif value == '':
        lines.append(TEMPLATE_EMPTY.format(
            indent, sign, key))

    else:
        lines.append(TEMPLATE_STYLISH.format(
            indent, sign, key, convert(value)))

    return '\n'.join(lines)


def render_dict(dict_: dict, depth: int) -> str:
    """

    :param dict_:
    :param depth:
    :return:
    """

    lines = []
    indent = '    ' * depth

    for key, value in sorted(dict_.items()):
        lines.append(render_line(key, value, ' ', depth))

    result = itertools.chain("{", lines, [indent + "}"])

    return '\n'.join(result)


def convert(value: Any) -> str:
    """

    :param value:
    :return:
    """

    if isinstance(value, bool):
        converted_value = str(value).lower()
    elif value is None:
        converted_value = 'null'
    else:
        converted_value = str(value)

    return converted_value
