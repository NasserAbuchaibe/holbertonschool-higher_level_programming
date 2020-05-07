#!/usr/bin/python3
def roman_to_int(roman_string):
    if str != type(roman_string) or roman_string is None:
        return 0
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
           'D': 500, 'M': 1000}
    num = 0
    for a, b in zip(roman_string, roman_string[1:]):
        if rom[a] >= rom[b]:
            num += rom[a]
        else:
            num -= rom[a]
    num += rom[roman_string[-1]]
    return num
