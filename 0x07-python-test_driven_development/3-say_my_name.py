#!/usr/bin/python3

"""This module defines the function say_my_name"""


def say_my_name(first_name, last_name=""):
    """Print `My name is <first_name> <last_name>

    Args:
        first_name (str)
        last_name (str): Defaults to empty string.

    Raises:
        TypeError: If either first_name or last_name is not string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f'My name is {first_name} {last_name}')
