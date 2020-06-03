#!/usr/bin/python3
""" 8-load_from_json_file.py """

import json


def load_from_json_file(filename):
    """ creates an Object from a “JSON file”

    Args:
        filename ([type]): [description]

    Returns:
        [type]: [description]
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
