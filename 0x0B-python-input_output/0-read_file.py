#!/usr/bin/python3
"""Defines a module that reads a text file"""


def read_file(filename=""):
    """Returns the input of a text file"""

    with open(filename, encoding='utf-8') as f:
        read_data = f.read()
        print(read_data, end="")
