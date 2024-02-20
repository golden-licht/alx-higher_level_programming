#!/usr/bin/python3

"""This module contains the definition of a Student class"""


class Student:
    """A class representing a student"""
    def __init__(self, first_name, last_name, age):
        """Instantiate a Student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of a Student instance

        If `attrs` is a list of strings,
        only attribute names contained in this list are retrieved
        """
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            new_dict = {x: y for x, y in self.__dict__.items() if x in attrs}
            return new_dict
        return self.__dict__
