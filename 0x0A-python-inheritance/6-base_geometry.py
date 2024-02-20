#!/usr/bin/python3

"""This module defines the class BaseGeometry"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """Raise an exception indicating it's not implemented"""
        raise Exception("area() is not implemented")
