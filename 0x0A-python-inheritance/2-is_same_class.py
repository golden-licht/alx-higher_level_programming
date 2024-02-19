#!/usr/bin/python3

"""This module defines the function is_same_class"""


def is_same_class(obj, a_class):
    """Return True if an object's exactly an instance of the specified class"""
    if (type(obj) is a_class):
        return True
    return False
