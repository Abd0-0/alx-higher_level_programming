#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for elm in row:
            print("{:d}".format(col), end=" " if elm != row[-1] else "")
        print()
