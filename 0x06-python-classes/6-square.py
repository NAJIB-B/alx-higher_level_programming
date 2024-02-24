#!/usr/bin/python3
""" This module defines a square class"""


class Square:
    """A square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    def area(self):
        """Return current area of the square"""
        return self.size * self.size

    @property
    def size(self):
        """Return's the size of the square"""
        return self.__size

    @size.setter
    def size(self, size):
        """sets the size of the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """Return current position of the square"""
        return self.__position

    @position.setter
    def position(self, position):
        """sets the position of the square"""

        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[0], int) or
        not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def my_print(self):
        """print the square using "#" """
        if self.size == 0:
            print("")
        else:
            [print("") for i in range(0, self.position[1])]
            for i in range(self.size):
                for k in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print("")
