#!/usr/bin/python3
"""This module defines a rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
"""Defines the Rectangle class"""
    def __init__(self, width, height):
        """initialization of the function"""
        super().integer_validator(type(self).__name__, width)
        super().integer_validator(type(self).__name__, height)
        self.__width = width
        self.__height = height
