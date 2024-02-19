#!/usr/bin/python3

""""This module contains the definition of the function, lookup"""


def lookup(obj):
    """Return list of available attributes and methods of an object

    Args:
        obj (Object): The object
    """
    return dir(obj)
