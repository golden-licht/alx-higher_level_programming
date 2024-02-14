#!/usr/bin/python3

"""This module defines the function add_integer"""


def add_integer(a, b=98):
    """Add two numbers; floats are first casted to int before operation.

    Args:
        a (int or float): First number.
        b (int or float): Second number. Defaults to 98.

    Raises:
        TypeError: If either of the numbers are not int or float.

    Returns:
        int: The sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
