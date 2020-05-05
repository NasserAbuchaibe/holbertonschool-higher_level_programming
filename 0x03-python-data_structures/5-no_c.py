#!/usr/bin/python3
def no_c(my_string):
    new_string = ''
    for i in my_string:
        if 'c' != i or 'C' != i:
            new_string += i
    return new_string 
