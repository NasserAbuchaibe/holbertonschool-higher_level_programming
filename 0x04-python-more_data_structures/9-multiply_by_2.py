#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_d = {}
    for k, v in a_dictionary.items():
        new_d[k] = v * 2
    return new_d
