#!/usr/bin/python3
"""A module for the rectangle class"""


class Rectangle:
    """A rectangular class"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Instatiation of a new Rectangle"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @property
    def width(self):
        """retrieves of width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """setting of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """setting the height"""
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
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """printable rectangle"""
        if (self.__width == 0 or self.__height == 0):
            return ("")
        result = []
        for i in range(self.__height):
            for j in range(self.__width):
                result.append("#")
            if i != (self.__height - 1):
                result.append("\n")
            row = ""
        return ("".join(result))

    def __repr__(self):
        string = "Rectangle(" + str(self.__width)
        string += ", " + str(self.__height) + ")"
        return (string)
