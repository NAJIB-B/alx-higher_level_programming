#!/usr/bin/python3
"""Defines a function that gives the dictionary
description of simple data structures"""


def class_to_json(obj):
    """Returns the returns the dictionary description
    with simple data structure (list, dictionary, string,
    integer and boolean) for JSON serialization of an object"""

    return obj.__dict__
