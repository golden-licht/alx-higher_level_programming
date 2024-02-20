#!/usr/bin/python3

"""This module defines the function, class_to_json"""


def class_to_json(obj):
    """Convert an instance of a class to a dictionary for JSON serialization

    Args:
        obj (Object): An instance of a class

    Returns:
        A dictionary representation of the obj's attributes
        suitable for JSON serialization.
    """
    return obj.__dict__
