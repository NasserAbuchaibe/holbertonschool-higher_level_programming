#!/usr/bin/python3
""" 2-read_lines.py """


def read_lines(filename="", nb_lines=0):
    """ reads n lines of a text file (UTF8) and prints it to stdout:

    Args:
        filename (str, optional): file to read. Defaults to "".
        nb_lines (int, optional): number lines ti read. Defaults to 0.
    """
    with open(filename, encoding='utf-8') as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        else:
            for x, line in enumerate(f):
                if x == nb_lines:
                    break
                print(line, end="")
