#!/usr/bin/python3
""" 4-append_write.py """


def append_write(filename="", text=""):
    """  appends a string at the end of a text file
         (UTF8) and returns the number of characters added:

    Args:
        filename (str, optional): file to add. Defaults to "".
        text (str, optional): str to add to filename. Defaults to "".

    Returns:
        [int]: number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
