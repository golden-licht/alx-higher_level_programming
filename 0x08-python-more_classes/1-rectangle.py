#!/usr/bin/python3

"""This class defines a class, Rectangle"""


class Rectangle:
    """A class to represent a rectangle.

    This class represents a rectangle with a given width and height.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the reactangle.
    """
    def __init__(self, width=0, height=0):
        """Initialize the Rectangle object with given width and height

        Args:
            width (int): The width of the rectangle. Defaults to zero.
            height (int): The height of the rectangle. Defaults to zero.

        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height is less than zero.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method to retrive the width of the rectangle

        Returns:
            int: The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """"Setter method to set the width of the rectangle

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If value is not an int.
            ValueError: If value is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method to retrive the height of the rectangle

        Returns:
            int: The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """"Setter method to set the height of the rectangle

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If value is not an int.
            ValueError: If value is less than zero.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
