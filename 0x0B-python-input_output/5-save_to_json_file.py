#!/usr/bin/python3
"""Defines function that write object to text
file"""


import json


def save_to_json_file(my_obj, filename):
    """This function writes object to text file"""

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
