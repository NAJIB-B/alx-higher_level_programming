#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if !matrix:
        return None
    for i in matrix:
        for j in i:
            print("{:d}".format(j))

