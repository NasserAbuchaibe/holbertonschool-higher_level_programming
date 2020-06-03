#!/usr/bin/python3
""" 3-write_file.py """
def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8)
        and returns the number of characters written:

    Args:
        filename (str, optional): file to write. Defaults to "".
        text (str, optional): text to write. Defaults to "".

    Returns:
        [int]: characters number
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
