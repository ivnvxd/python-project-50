import json
from typing import Any

from gendiff.constants import (
    ADDED,
    REMOVED,
    UNCHANGED,
    UPDATED,
    NESTED
)


def make_json(diff: list) -> str:
    """
    Render the difference tree in "json" format.

    :param diff: Difference tree.
    :return: String of difference visualization in "json" format.
    """

    def iter_(data: Any) -> dict:

        diff_dict = {}
        data.sort(key=lambda node: node['key'])

        for node in data:

            if node['type'] in [REMOVED, UNCHANGED]:
                diff_dict[node['key']] = {
                    'value': node['old_value']
                }

            elif node['type'] == ADDED:
                diff_dict[node['key']] = {
                    'value': node['new_value']
                }

            elif node['type'] == UPDATED:
                diff_dict[node['key']] = {
                    'value': node['old_value'],
                    'new value': node['new_value']
                }

            elif node['type'] == NESTED:
                diff_dict[node['key']] = {
                    'value': iter_(node['children'])
                }

            diff_dict[node['key']]['type'] = node['type']

        return diff_dict

    result = json.dumps(iter_(diff), indent=4)

    return result
