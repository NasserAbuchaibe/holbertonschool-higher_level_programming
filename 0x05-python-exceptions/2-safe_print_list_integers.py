#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        cont = 0
        for y in range(x):
            if type(my_list[y]) == int:
                print("{:d}".format(my_list[y]), end="")
                cont += 1
        print("")
        return cont
    except (ValueError, TypeError):
        pass
