#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return "None"
    max_n = my_list[0]
    for i in my_list:
        if max_n < i:
            max_n = i
    return max_n
