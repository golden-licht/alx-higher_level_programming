#!/usr/bin/python3

"""This module defines the class BaseGeometry"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """Raise an exception indicating it's not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check if a `value` with identifier, `name`, is a positive integer

        Args:
            name (str): Identifier for value
            value (int): The value to be validated
        Raises:
            TypeError: If value is not integer
            ValueError: If value is less than zero
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
