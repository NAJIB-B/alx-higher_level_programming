#!/usr/bin/python3
"""Defines a base geometery class"""


class BaseGeometry:
    """Represent the base geometery"""
    def area(self):
        """Defines an empty area function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Defines a function that validates integer"""
        if value is None and name is None:
            raise TypeError("integer_validator() missing 2 required positional\
                    arguments: 'name' and 'value'")
        if value is None:
            raise TypeError("integer_validator() missing 1 required\
                    positional argument: 'value'")
        if type(value) is not int:
            msg = name + " must be an integer"
            raise TypeError(msg)

        if value <= 0:
            msg = name + " must be greater than 0"
            raise ValueError(msg)
