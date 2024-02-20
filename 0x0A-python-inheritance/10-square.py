#!/usr/bin/python3

"""This module defines the class Square"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A class representing a square"""
    def __init__(self, size):
        """Initialize a square object"""
        super().__init__(size, size)
