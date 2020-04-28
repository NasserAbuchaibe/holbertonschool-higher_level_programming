#!/usr/bin/env python3


def print_last_digit(number):
    if number < 0:
        number = abs(number)
    aux = number % 10
    print("{:d}".format(aux), end="")
    return aux
