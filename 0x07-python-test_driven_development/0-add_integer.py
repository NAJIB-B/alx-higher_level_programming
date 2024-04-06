#!/usr/bin/python3
    
"""
This module adds integers together
"""


def add_integer(a, b=98):
    """Returns the addition of two numbers
    and if b is not given it defaults to 98
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b

