#!/usr/bin/python3

""" add_integer - function that adds 2 integers."""


def add_integer(a, b=98):

    """
    function that adds 2 integers

    Args:
    a: Number integer
    b: Number integer which by default is 98 if an argument is
       not passed to the parameter
    Return:
    an integer resulting from a + b

    """

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    if type(a) != int:
        raise TypeError("a must be an integer")
    elif type(b) != int:
        raise TypeError("b must be an integer")
    else:
        return a + b
