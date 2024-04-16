#!/usr/bin/python3
"""Defines a function thtat appends to a file"""


def append_write(filename="", text=""):
    """Returns the number of characters added to 
    the file"""

    with open(filename, 'a+', encoding='utf-8') as f:
        return (f.write(text))
