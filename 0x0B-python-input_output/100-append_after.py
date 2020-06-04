#!/usr/bin/python3
""" 100-append_after.py """


def append_after(filename="", search_string="", new_string=""):
    """[summary]

    Args:
        filename (str, optional): [description]. Defaults to "".
        search_string (str, optional): [description]. Defaults to "".
        new_string (str, optional): [description]. Defaults to "".
    """
    with open(filename, "r+", encoding="utf-8") as f:
        list_text = f.readlines()

    cont_lines = 0
    with open(filename, "w", encoding="utf-8") as f:
        for line in list_text:
            cont_lines += 1
            if search_string in line:
                list_text.insert(cont_lines, new_string)

        for line in list_text:
            f.write(line)
