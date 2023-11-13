#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    lista = []
    for i in matrix:
        lista.append(list(map(lambda x: x * x, i)))
    return (lista)
