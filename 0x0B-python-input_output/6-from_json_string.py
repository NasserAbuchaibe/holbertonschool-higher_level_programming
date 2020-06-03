#!/usr/bin/python3
""" 6-from_json_string.py """


import json


def from_json_string(my_str):
    """ turns an object (Python data structure) represented by a JSON string:
    Args:
        my_str ([str]): [description]

    Returns:
        [type]: [description]
    """
    return json.loads(my_str)
