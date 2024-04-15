#!/usr/bin/python3
"""Defines a class Square tha inherits for Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Reprsents a Square using Rectangle"""

    def __init__(self, size):
        """initializes a new square

        Args:
            size (int): the size of the square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns the area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """Return the print() and str() representation of a Square."""

        output = "[Rectangle] " + str(self.__size)\
            + "/" + str(self.__size)
        return output
