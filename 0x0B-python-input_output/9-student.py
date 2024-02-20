#!/usr/bin/python3

"""This module contains the definition of a Student class"""


class Student:
    """A class representing a student"""
    def __init__(self, first_name, last_name, age):
        """Instantiate a Student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary representation of a Student instance"""
        return self.__dict__
