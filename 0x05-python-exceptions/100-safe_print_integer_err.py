#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as mo:
        print("Exception: {}".format(mo))
        return False
