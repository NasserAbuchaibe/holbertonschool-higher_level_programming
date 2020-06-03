#!/usr/bin/python3
""" 7-save_to_json_file.py """
import json


def save_to_json_file(my_obj, filename):
    """[summary]

    Args:
        my_obj ([type]): [description]
        filename ([type]): [description]
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
