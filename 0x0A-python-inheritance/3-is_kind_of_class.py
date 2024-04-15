#!/usr/bin/python3
"""Checks if an object is an instance of
another object"""


def is_kind_of_class(obj, a_class):
    """Returns true if obj is an instance of
    a_class and false otherwise"""

    if isinstance(obj, a_class):
        return True
    return False
