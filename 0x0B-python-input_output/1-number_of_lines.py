#!/usr/bin/python3
""" 1-number_of_lines.py """


def number_of_lines(filename=""):
    """returns the number of lines of a text file

    Args:
        filename (str, optional): file to count number lines. Defaults to "".

    Returns:
        [int]: number lines of file
    """
    with open(filename, encoding='utf-8') as f:
        cont = 0
        for line in f:
            cont += 1
        return cont
