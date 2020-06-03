#!/usr/bin/python3
""" 0-read_file.py """


def read_file(filename=""):
    """ function that reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str, optional): file to reads and print. Defaults to "".
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
