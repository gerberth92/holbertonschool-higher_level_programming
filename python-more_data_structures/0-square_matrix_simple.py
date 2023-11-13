#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    l = []
    for i in matrix:
        l.append(list(map(lambda x: x * x, i)))
    return (l)
