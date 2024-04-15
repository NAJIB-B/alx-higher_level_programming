#!/usr/bin/python3
"""This module contains a class that inherits from
the List class"""


class MyList(list):
    """inherits from the List class"""

    def print_sorted(self):
        """sorts a list"""
        print(sorted(self))
