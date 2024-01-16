#!/usr/bin/python3
for i in range(89):
    if i / 10 >= i % 10:
        continue
    if i < 10:
        i = '0' + str(i)
    print("{},".format(i), end=" ")
print(89)
