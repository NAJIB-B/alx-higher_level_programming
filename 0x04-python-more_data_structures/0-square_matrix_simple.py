#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []

    for i in matrix:
        child_matrix = []
        for j in i:
            child_matrix.append(j ** 2)
        new_matrix.append(child_matrix)
    return new_matrix
