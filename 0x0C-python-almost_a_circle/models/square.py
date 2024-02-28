#!/usr/bin/python3

from models.rectangle import Rectangle

"""This module contains definition for the class, `Square`"""


class Square(Rectangle):
    """A class representing a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiate a `Square` object"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size attribute"""
        self.width = value

    def __str__(self):
        """Update the `str` method"""
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    def update(self, *args, **kwargs):
        """Update the attributes of a `Square` instance"""
        attributes = ['id', 'size', 'x', 'y']
        if len(args):
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Return dictionary representation of the
        attribute: value pairs of a `Square` instance"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
