#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cont = 0
    for y, i in enumerate(my_list):
        try:
            if x > y:
                print("{}".format(i), end="")
                cont += 1
        except IndexError:
            return cont
    print()
    return cont
