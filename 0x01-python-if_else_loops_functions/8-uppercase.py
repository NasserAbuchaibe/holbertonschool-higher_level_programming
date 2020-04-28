#!/usr/bin/env python3
def uppercase(str):
    for alf in str:
        aux = ord(alf)
        if aux >= 97 and aux <= 122:
            aux -= 32
        print("{:c}".format(aux), end="")
    print()
