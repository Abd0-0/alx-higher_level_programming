#!/usr/bin/python3
def uppercase(str):
    for w in str:
        if ord(w) >= ord('a') and ord(w) <= ord('z'):
            char = chr(ord(w) - 32)
        else:
            char = w
        print("{:s}".format(char), end="")
    print()
