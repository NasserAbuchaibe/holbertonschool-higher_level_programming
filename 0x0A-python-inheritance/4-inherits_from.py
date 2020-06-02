#!/usr/bin/python3
"""function that returns True if the object is an instance of a class that
   inherited (directly or indirectly) from the specified class;
   otherwise False.
"""


def inherits_from(obj, a_class):
    """ 4-inherits_from.py

    Args:
        obj (object): object to check
        a_class (class): class to check

    Returns:
        [bool]: True if the object is an instance of a class that
        inherited from the specified class; otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
