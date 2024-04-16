#!/usr/bin/python3


import json
"""Defines a function that represents objects in string
format"""


def to_json_string(my_obj):
    """Returns the string representation of a json
    object"""

    return (json.dumps(my_obj))
