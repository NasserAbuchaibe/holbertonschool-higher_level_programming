#!/usr/bin/python3
def best_score(a_dictionary):
    max_ = 0
    if not a_dictionary:
        return "None"
    for k, v in a_dictionary.items():
        if max_ < v:
            max_ = v
    for k, v in a_dictionary.items():
        if max_ == v:
            return k
