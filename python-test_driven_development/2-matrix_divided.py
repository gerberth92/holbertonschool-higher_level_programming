#!/usr/bin/python3
"""
Este modulo tiene una funcion de division.
"""


def matrix_divided(matrix, div):
    """
    Esta funcion realiza la division de una matriz.

    Args:
        matriz (list): esta es una lista de listas.
        div (int, float): este es el divisor puede ser un (int) o float).

    Raises:
        TypeError:
            Si (div) no es un entero o float.
            Si div es igual a 0.
            Si la matriz no es una lista.
            Si la matriz no tiene listas dentro.
            Si los elementos de las listas no son de tipo (int) o (float).
            Si las listas internas no tiene el mismo tamaño.

    Returns:
        new (list): una nueva lista de listas con las divisiones.
    """
    msj = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not matrix or not isinstance(matrix, list):
        raise TypeError(msj)

    len_element = 0
    new = []

    for element in matrix:
        if not element or not isinstance(element, list):
            raise TypeError(msj)
        if len_element != 0 and len(element) != len_element:
            raise TypeError("Each row of the matrix must have the same size")
        for num in element:
            if not isinstance(num, int) and not isinstance(num, float):
                raise TypeError(msj)

        len_element = len(element)

        new.append(list(map(lambda x: round(x / div, 2), element)))

    return (new)
