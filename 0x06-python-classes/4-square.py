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

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        self.__size = size

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size**2

    @property
    def size(self):
        """Getter method to retrieve the size of the square.

        Returns:
            int: The size of the square's side.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size of the square.

        Args:
            value (int): The new size of the square's side.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
