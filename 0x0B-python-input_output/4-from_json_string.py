#!/usr/bin/python3
"""Defines a function that represents json in object
format"""


import json


def from_json_string(my_str):
    """Returns the object representation of a json string"""

    return (json.loads(my_str))
