#!/usr/bin/python3
""" 5-to_json_string.py """


import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string):

    Args:
        my_obj (object):
    Returns:
        [json string]: [description]
    """
    return json.dumps(my_obj)
