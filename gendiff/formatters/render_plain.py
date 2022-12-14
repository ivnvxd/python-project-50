from typing import Any

from gendiff.constants import (
    ADDED,
    REMOVED,
    UPDATED,
    NESTED,

    TEMPLATE_PLAIN_ADDED,
    TEMPLATE_PLAIN_REMOVED,
    TEMPLATE_PLAIN_UPDATED,
    TEMPLATE_PLAIN_PATH
)


def make_plain(diff: list, source: str = '') -> str:
    """
    Render the difference tree in "plain" format.

    :param diff: Difference tree.
    :param source: Full path to current node.
    :return: String of difference visualization in "plain" format.
    """

    lines = []
    diff.sort(key=lambda node: node['key'])

    for node in diff:

        if source:
            path = TEMPLATE_PLAIN_PATH.format(source,
                                              node['key'])
        else:
            path = node['key']

        if node['type'] == REMOVED:
            lines.append(
                TEMPLATE_PLAIN_REMOVED.format(path)
            )

        elif node['type'] == ADDED:
            lines.append(
                TEMPLATE_PLAIN_ADDED.format(path,
                                            convert(node['new_value']))
            )

        elif node['type'] == UPDATED:
            lines.append(
                TEMPLATE_PLAIN_UPDATED.format(path,
                                              convert(node['old_value']),
                                              convert(node['new_value']))
            )

        elif node['type'] == NESTED:
            lines.append(
                make_plain(node['children'], path)
            )

    result = '\n'.join(lines)

    return result


def convert(value: Any) -> str:
    """
    Converts input data to unify it while comparing.

    :param value: Value to be converted.
    :return: String in unified format.
    """

    if isinstance(value, bool):
        converted = str(value).lower()
    elif isinstance(value, int):
        converted = str(value)
    elif isinstance(value, dict):
        converted = '[complex value]'
    elif value is None:
        converted = 'null'
    else:
        converted = f"'{str(value)}'"

    return converted
