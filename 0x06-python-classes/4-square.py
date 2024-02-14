#!/usr/bin/python3
""" This module defines a square class
    with a private instance attribute
    size
    """


class Square:
    """A square class"""

    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.size * self.size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
