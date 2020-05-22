#!/usr/bin/python3

""" say_my_name """


def say_my_name(first_name, last_name=""):
    """
    function that prints My name is <first name> <last name>

    Args:
    first_name: string
    last_name: string

    Return: void

    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    if len(first_name) == 0:
        raise TypeError("say_my_name() missing 1 required positional argument:"
                        " 'first_name'")

    print("My name is {:s} {:s}".format(first_name, last_name))
