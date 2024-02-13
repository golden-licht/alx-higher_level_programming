#!/usr/bin/python3

"""This class defines a class, Rectangle"""


class Rectangle:
    """A class to represent a rectangle.

    This class represents a rectangle with a given width and height.

    Attributes:
        number_of_instances (int): The number of rectangle objects spawned.
        print_symbol (any): The symbol used for printing a rectangle object.
        width (int): The width of the rectangle.
        height (int): The height of the reactangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle object with given width and height

        Each time an object is created, number_of_instances is incremented by 1

        Args:
            width (int): The width of the rectangle. Defaults to zero.
            height (int): The height of the rectangle. Defaults to zero.

        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height is less than zero.
        """
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

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

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of the rectangle,
        using the value of print_symbol attribute"""
        if self.width == 0 or self.height == 0:
            return ""
        symbol = str(self.print_symbol)
        rows = [symbol * self.width for _ in range(self.height)]
        return '\n'.join(rows)

    def __repr__(self):
        """Returns a string representation of the object
        that can be used to recreate it"""
        return f"{self.__class__.__name__}({self.width}, {self.height})"

    def __del__(self):
        """Delete a Rectangle object"""
        print("Bye rectangle...")
        self.__class__.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare two Rectangle objects based on area.

        Args:
        rect_1 (Rectangle): A rectangle object.
        rect_2 (Rectangle): A rectangle object.

        Returns:
            Rectangle: The larger of rect_1 and rect_2 by area.
            If equal, rect_1
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() >= rect_2.area()):
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new instance with both width and height equal to size"""
        return cls(size, size)
