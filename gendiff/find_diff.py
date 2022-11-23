from typing import Any

from gendiff.constants import (
    ADDED,
    REMOVED,
    UNCHANGED,
    UPDATED,
    NESTED,
)


def get_diff_tree(file1: dict, file2: dict) -> list:
    """

    :param file1:
    :param file2:
    :return:
    """

    all_keys = sorted(set(file1.keys()) | set(file2.keys()))
    tree = []

    for key in all_keys:

        if key in file1 and key not in file2:
            node = add_node(key, REMOVED, old_value=file1[key])

        elif key not in file1 and key in file2:
            node = add_node(key, ADDED, new_value=file2[key])

        elif file1[key] == file2[key]:
            node = add_node(key, UNCHANGED, old_value=file1[key])

        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            child = get_diff_tree(file1[key], file2[key])
            node = add_node(key, NESTED, children=child)

        else:
            node = add_node(key, UPDATED, new_value=file2[key],
                            old_value=file1[key])

        tree.append(node)

    return tree


def add_node(key: Any, node_type: str, new_value: Any = None,
             old_value: Any = None, children: Any = None) -> dict:
    """

    :param key:
    :param node_type:
    :param new_value:
    :param old_value:
    :param children:
    :return:
    """

    node = {
        'key': key,
        'type': node_type,
        'old_value': old_value,
        'new_value': new_value,
    }

    if children:
        node['children'] = children

    return node
