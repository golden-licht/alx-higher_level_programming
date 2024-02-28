#!/usr/bin/python3

"""This module contains definition for the class, `Rectangle`"""
from models.base import Base


class Rectangle(Base):
    """A class representing a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiate a `Rectangle` object"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """"Setter for height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """"Setter for x attribute"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y attribute"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate area of the `Rectangle` instance"""
        area = self.width * self.height
        return area

    def __str__(self):
        """Update the `str` method"""
        return (f'[Rectangle] ({self.id}) {self.x}/{self.y} -' +
                f' {self.width}/{self.height}')

    def display(self):
        """Display the `Rectangle` instance using #'s"""
        for _ in range(self.y):
            print()
        for row in range(self.height):
            print(self.x * " ", end="")
            print(self.width * "#")

    def to_dictionary(self):
        """Return dictionary representation of the attribute: value
        pairs of a `Rectangle` instance"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def update(self, *args, **kwargs):
        """Update the attributes of a `Rectangle` instance"""
        attributes = ['id', 'width', 'height', 'x', 'y']
        if len(args):
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)
