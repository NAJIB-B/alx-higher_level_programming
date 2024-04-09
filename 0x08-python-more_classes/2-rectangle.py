#!/usr/bin/python3

"""This module describes a Rectangle
using python class"""


class Rectangle:

    """This is a rectangle class"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrives the width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrives the height"""
        return (self.__height)

    @width.setter
    def height(self, value):
        """sets the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
         """return the are of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
         """return the perimeter of the rectangle"""
        if (self.__width == 0 or self.__height == 0):
            return (0)
        return ((self.__width + self.__height) * 2)
