#!/usr/bin/python3
"""
Defines a function for integer addition
"""


def add_integer(a, b=98):
    """The function add two numbers
    Args:
        a: (int/float) the first number
        b: (int/float) the second number
    Raises:
        TypeError if a or b is not int or float
    Returns:
        Addition of a and b
    """

    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
