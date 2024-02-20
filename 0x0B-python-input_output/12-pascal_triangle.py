#!/usr/bin/python3

"""This module contains the definition of the function, pascal_triangle"""


def pascal_triangle(n):
    """Return a list of lists of integers
    representing the Pascal’s triangle of n

    approach:

    pascal_list(n=1) is [[1]].
    n represents the height of the triangle.
    each inner list starts and ends with value=1.
    the values of the the remaining index of the inner list,
    at a certain height is a function of the values from the row above it.

    first find the inner list at each height, then append this list
    to the pascal list.
    """
    if n <= 0:
        return []

    pascal_list = [[1]]

    for height in range(1, n):
        inner_list = [1]

        for i in range(0, height - 1):
            left = pascal_list[height - 1][i]
            right = pascal_list[height - 1][i + 1]
            inner_list.append(left + right)
        inner_list.append(1)
        pascal_list.append(inner_list)
    return pascal_list
