#!/usr/bin/python3
"""Checks if an object is an instance
of a class"""


def is_same_class(obj, a_class):
    """Returns true if obj is an instance of
    a  class and false otherwise"""

    if type(obj) is a_class:
        return True
    return False
