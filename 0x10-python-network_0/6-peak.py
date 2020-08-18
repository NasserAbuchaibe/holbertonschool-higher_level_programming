#!/usr/bin/python3
""" Test function find_peak """


def find_peak(list_of_integers):
    """[summary]

    Args:
        list_of_integers ([type]): [description]
    """
    if not list_of_integers:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    list_of_integers.sort()
    return list_of_integers[-1]
