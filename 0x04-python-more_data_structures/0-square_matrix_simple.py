#!/usr/bin/python3
def pow_(num):
    return num * num

def square_matrix_simple(matrix=[]):
    matrix_n = []
    for i in matrix:
            matrix_n.append(list(map(pow_, i)))
    return matrix_n
