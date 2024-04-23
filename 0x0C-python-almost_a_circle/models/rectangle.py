#!/usr/bin/python3
"""Defines a rectangle model"""

from models.base import Base


class Rectangle(Base):
    """Represents a rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes an instance of a Rectangle"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns the value of width"""

        return self.__width

    @width.setter
    def width(self, width):
        """sets the value of width"""
        self.if_int("width", width)
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Returns the value of height"""
        return self.__height

    @height.setter
    def height(self, height):
        """sets the value of height"""
        self.if_int("height", height)
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Returns the value of x"""
        return self.__x

    @x.setter
    def x(self, x):
        """sets the value of x"""
        self.if_int("x", x)
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Returns the value of y"""
        return self.__y

    @y.setter
    def y(self, y):
        """sets the value of y"""
        self.if_int("y", y)
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def if_int(self, name, value):
        """Checks if value is int"""
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")

    def area(self):
        """Returns the area of the rectangle"""
        return self.height * self.width

    def display(self):
        """prints out the rectangle"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            for _ in range(self.x):
                print(" ", end="")
            for _ in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Changes the printable version of rectangle"""
        string = "[Rectangle] ({}) {}/{} - {}/{}"
        .format(self.id, self.x, self.y, self.width, self.height)
        return string

    def update(self, *args, **kwargs):
        """Updates the attribute for the rectangle class"""

        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

        if len(args) > 0:
            self.id = args[0]

        if len(args) > 1:
            self.width = args[1]

        if len(args) > 2:
            self.height = args[2]

        if len(args) > 3:
            self.x = args[3]

        if len(args) > 4:
            self.y = args[4]

    def to_dictionary(self):
        """Returns the dictionary representation of Rectangle"""

        initial_dict = self.__dict__
        new_dict = {}

        for key, value in initial_dict.items():
            if key.startswith("_Rectangle__"):
                new_key = key.replace("_Rectangle__", "")
                new_dict[new_key] = value
            else:
                new_dict[key] = value
        return new_dict
