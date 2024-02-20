#!/usr/bin/python3
"""This module defines the a class, Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that represents a rectangle"""
    def __init__(self, width, height):
        """Initialize a new Rectangle object."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
