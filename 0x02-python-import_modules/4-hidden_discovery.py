#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for str1 in dir(hidden_4):
        if str1[0] != '_':
            print(str1)
