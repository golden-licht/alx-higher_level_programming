#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = abs(number) % 10  # last digit
if (number < 0):
    ld *= -1
print(f"Last digit of {number:d} is {ld:d} and is", end=' ')

if ld > 5:
    print("greater than 5")
elif ld == 0:
    print("0")
else:
    print("less than 6 and not 0")
