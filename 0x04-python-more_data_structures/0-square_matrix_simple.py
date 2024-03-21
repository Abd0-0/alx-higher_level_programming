#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = matrix.copy()
    for i in range(len(matrix):
            new[i] = list(map(lambda n: n**2, matrix[i]))

    return new
