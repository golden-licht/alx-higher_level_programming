#!/usr/bin/python3

"""Module defining a Square class."""


class Square:
    """A class to represent a square.

    This class represents a square with a given size.

    Attributes:
        size (int): The side length of the square.
    """

    def __init__(self, size=0):
        """Initialize the Square object with a given size.

        Args:
            size (int): The size of the square's side. Defaults to zero.
        """
        self.__size = size
