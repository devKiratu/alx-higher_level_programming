#!/usr/bin/python3
def uppercase(str):
    for i in str:
        c = i
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(i) - 32)
        print("{}".format(c), end="")
    print("")
