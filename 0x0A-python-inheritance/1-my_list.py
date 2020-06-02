#!/usr/bin/python3
"""Module for class Mylist """


class MyList(list):
    """Class Mylist

    Args:
        list (list): class from which Mylist inherits
    """
    def print_sorted(self):
        print(sorted(self))
