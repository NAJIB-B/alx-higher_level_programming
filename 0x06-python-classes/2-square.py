#!/usr/bin/python3
""" This module defines a square class
    with a private instance attribute
    size
    """


class Square:
    """A square class"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise Value("size must be >= 0")
        self.__size = size
