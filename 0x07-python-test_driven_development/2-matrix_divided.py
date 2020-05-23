#!/usr/bin/python3

""" matrix_divided - that divides all elements of a matrix."""


def matrix_divided(matrix, div):

    """
    function that divides all elements of a matrix.

    Args:
    matrix: matrix of integers or floats,
    div:  must be a number (integer or float)

    Return:  new matrix
    """

    if div == float('inf') or div == -float('inf'):
        raise OverflowError("cannot convert float infinity to integer")
    if div == float('NaN') or div != div:
        raise ValueError("cannot convert float NaN to integer")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    for lists in matrix:
        if len(lists) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if type(matrix[x][y]) == str:
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
    return [[float("{:.2f}".format(y/div)) for y in x] for x in matrix]
