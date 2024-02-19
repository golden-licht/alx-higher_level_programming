#!/usr/bin/python3

"""This module defines the function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a class"""
    if (isinstance(obj, a_class)):
        return True
    return False
