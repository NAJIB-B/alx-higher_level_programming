#!/usr/bin/python3
"""This model defines a class Base"""


class Base:
    """Represent a class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes an instance of the base class

        Args:
            id: the id of the instance
        """

        if id is not None:
            self.id = id
        else:
             Base.__nb_objects += 1
             self.id = Base.__nb_objects

