#!/usr/bin/python3

"""This module defines a function that divides a matrix"""


def matrix_divided(matrix, div):
    """this function divides all element of a matrix
    Args:
        matrix (list): the matrix to be divided
        div (int/float): the number to divide the matrix by
    Raises:
        TypeError if matrix is not a list of lists, or if the
        lists in the list are not the same size
    Return:
        returns a new matrix with the divided values
    """
    if div is None or matrix is None:
        raise TypeError("matrix must be a matrix
                        (list of lists) of integers/floats")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix
                        (list of lists) of integers/floats")
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError("matrix must be a matrix
                            (list of lists) of integers/floats")
        for j in i:
            if not (isinstance(j, int) or isinstance(j, float)):
                raise TypeError("matrix must be a matrix
                                (list of lists) of integers/floats")
    matrix_len = len(matrix[0])

    for i in matrix:
        if len(i) != matrix_len:
            raise TypeError("Each row of the
                            matrix must have the same size")

    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []

    for i in matrix:
        divided_matrix = []
        for j in i:
            divided_matrix.append(round(j/div, 2))
        new_matrix.append(divided_matrix)

    return (new_matrix)
