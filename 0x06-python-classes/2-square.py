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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
