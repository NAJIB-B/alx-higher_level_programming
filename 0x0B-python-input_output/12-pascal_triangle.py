#!/usr/bin/python3
"""Defines a function that generates a
pascal triangle"""


def pascal_triangle(n):
    """Returns the pascal triangle of a number
    in a list of lists format"""
    if n <= 0:
        return []
    triangle = []
    last_row = []
    row = 0
    if n >= 1:
        last_row.append(1)
        triangle.append(last_row)
        row += 1
    while row < n:
        new_row = []
        new_row.append(1)
        for i in range(len(last_row)):
            if i < (len(last_row) - 1):
                new_row.append(last_row[i] + last_row[i + 1])
            else:
                new_row.append(1)
                triangle.append(new_row)
                row += 1
                last_row = new_row

    return triangle
