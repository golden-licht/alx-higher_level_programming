#!/usr/bin/python3
def print_last_digit(number):
    ld = abs(number) % 10   # last digit
    print("{}".format(ld), end="")
    return ld
