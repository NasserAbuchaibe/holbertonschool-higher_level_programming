#!/usr/bin/python3
""" 14-pascal_triangle.py """


def pascal_triangle(n):
    """[summary]

    Args:
        n ([type]): [description]

    Returns:
        [type]: [description]
    """
    if n <= 0:
        return []
    row = [1]
    init = [0]

    for x in range(n):
        print(row)
        row = [x + y for x, y in zip(row + init, init + row)]
