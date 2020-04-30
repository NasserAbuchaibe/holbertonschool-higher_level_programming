#!/usr/bin/python3
sum1 = 0
if __name__ == "__main__":
    import sys
    size = len(sys.argv)
    for x in range(1, size):
        sum1 = sum1 + int(sys.argv[x])
print("{}".format(sum1))
