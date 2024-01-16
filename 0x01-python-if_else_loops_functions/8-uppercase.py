#!/usr/bin/python3
def uppercase(str):
    s = ""
    for char in str:
        if 97 <= ord(char) <= 122:
            s += chr(ord(char) - 32)
        else:
            s += char
    print(s)
