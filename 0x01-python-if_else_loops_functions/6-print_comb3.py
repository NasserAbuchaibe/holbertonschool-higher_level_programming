#!/usr/bin/python3
for x in range(0, 8):
    for y in range(x + 1, 10):
        print("{:d}{:d}, ".format(x, y), end="")
print("{:02d}".format(89))
