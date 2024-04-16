#!/usr/bin/python3
"""Defines a module that writes to a file"""


def write_file(filename="", text=""):
    """Returns number of bytes written to a file"""

    with open(filename, 'w', encoding='utf-8') as f:
        written_bytes = f.write(text)
        return (written_bytes)
