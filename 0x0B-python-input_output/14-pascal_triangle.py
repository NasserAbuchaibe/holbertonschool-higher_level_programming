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

    row = []
    for num in range(1, n + 1):
        new_row = []
        for i in range(num):
            if i == 0 or i == num - 1:
                new_row.append(1)
            else:
                new_row.append(row[num - 2][i] + row[num - 2][i - 1])
        row.append(new_row)

    return row
