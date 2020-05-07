#!/usr/bin/python3
def uniq_add(my_list=[]):
    auxl = []
    sum_ = 0
    for i in my_list:
        if i not in auxl:
            auxl.append(i)
    for x in auxl:
        sum_ += x
    return sum_
