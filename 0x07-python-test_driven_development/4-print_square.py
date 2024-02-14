#!/usr/bin/python3

"""This module defines the function print_square"""


def print_square(size):
    """Print a square using #s

    Args:
        size (int): The side length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than zero.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    rows = ["#" * size for _ in range(size)]
    print("\n".join(rows))
