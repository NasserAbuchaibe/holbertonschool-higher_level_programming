#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        cont = 0
        for i in my_list[:x]:
            print("{}".format(i), end="")
            cont += 1
        print("")
        return cont
    except Error:
        print("ERROR")
