#!/usr/bin/python3
""" Test function find_peak """


def find_peak(list_of_integers):
    """[summary]

    Args:
        list_of_integers ([type]): [description]
    """
    if not list_of_integers:
        return None
    return max(list_of_integers)
