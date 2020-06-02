#!/usr/bin/python3
"""2-is_same_class.py
"""


def is_same_class(obj, a_class):
    """[summary]

    Args:
        obj (object): object to check
        a_class (class): class to check
    """
    return (type(obj) == a_class)
