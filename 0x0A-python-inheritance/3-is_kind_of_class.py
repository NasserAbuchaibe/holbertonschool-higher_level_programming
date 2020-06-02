#!/usr/bin/python3
"""3-is_kind_of_class.py
"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of,
       or if the object is an instance of a class that inherited from

    Args:
        obj (object): object to check
        a_class (class): class to check
    """
    return (isinstance(obj, a_class))
