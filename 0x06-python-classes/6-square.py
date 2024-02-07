#!/usr/bin/python3

"""Module defining a Square class."""


class Square:
    """A class to represent a square.

    This class represents a square with a given size and position.

    Attributes:
        size (int): The side length of the square.
        position (tuple): The position of the square's top-left corner.
            Defaults to (0, 0).
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the Square object with a given size and position.

        Args:
            size (int): The size of the square's side. Defaults to zero.
            position (tuple): The position of the square's top-left corner.
                Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or if position is not a tuple
                of 2 integers.
            ValueError: If size is negative.
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Getter method to retrieve the position of the square.

        Returns:
            tuple: The position of the square's top-left corner.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method to set the position of the square.

        Args:
            value (tuple): The new position of the square's top-left corner.

        Raises:
            TypeError: If value is not a tuple of 2 integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size**2

    def my_print(self):
        """Print a square using '#' characters.

        If the size is 0, prints an empty line. Otherwise, prints a square
        with sides of length equal to the size attribute and position according
        to the position attribute.
        """
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
