#!/usr/bin/python3

""" text_indentation - Function that prints a text with 2 new lines
    after each of these characters: . ? and :
"""


def text_indentation(text):
    """
    Args:
    -----
    text: must be a string

    Return: void
    ------
    """
    sep = ('.', '?', ':')
    aux = ""
    x = 0
    if type(text) != str:
        raise TypeError("text must be a string")

    if len(text) == 0:
        print()
    else:
        while x < len(text):
            if text[x] not in sep:
                aux += text[x]
            else:
                aux += text[x]
                print(aux)
                print()
                aux = ""
                while x < (len(text) - 1) and text[x + 1] == " ":
                    x += 1
            x += 1
    print(aux, end="")
