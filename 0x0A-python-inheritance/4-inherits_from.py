#!/usr/bin/python3

"""This module defines the function inherits_from"""


def inherits_from(obj, a_class):
    """Check if an object's class is a subclass of the specified class"""

    return (issubclass(obj.__class__, a_class) and type(obj) is not a_class)
