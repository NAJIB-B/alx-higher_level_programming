#!/usr/bin/python3

"""This module defines a function that says a person's name"""


def say_my_name(first_name, last_name=""):
    """Prints the first name and last name to console"""

    if first_name is None:
        raise TypeError("first_name must be a string")
    if last_name is None:
        raise TypeError("last_name must be a string")
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
