#!/usr/bin/env python3


def print_last_digit(number):
    aux = abs(number) % 10
    print("{:d}".format(aux), end="")
    return aux
