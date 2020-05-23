#!/usr/bin/python3

""" print_square - function that prints a square """


def print_square(size):
    """
    Arg:
    ---

    size: size is the size length of the square.
          Must be an integer.
          Must be greater than or equal to 0.

    Return: void

    """

    if (type(size) == float and size < 0):
        raise TypeError("size must be an integer")

    if type(size) != int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print()
    else:
        for x in range(size):
            print("#" * size)
