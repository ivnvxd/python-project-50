from typing import Any

from gendiff.constants import (
    ADDED,
    REMOVED,
    UNCHANGED,
    UPDATED,
    NESTED,
)


def get_diff_tree(file1: dict, file2: dict) -> list:
    """Calculates the difference between two files.

    :param file1: First file as the Python dict object.
    :param file2: Second file as the Python dict object.
    :return: Difference tree as a list of dictionaries.
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
    Accumulates all the parameters of one node and returns it in a dict.

    :param key: Name of the node.
    :param node_type: Type of node (added, removed etc.)
    :param new_value: New value of given key.
    :param old_value: Previous value of given key.
    :param children: List of children of current node if there are any.
    :return: Dict of node parameters.
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
