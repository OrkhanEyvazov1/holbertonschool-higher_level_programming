#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for list_ in matrix:
        for i, e in enumerate(list_):
            print("{:d}".format(e), end=' ' if i != len(list_) - 1 else '')
        print()
