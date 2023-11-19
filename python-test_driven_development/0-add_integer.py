#!/usr/bin/python3
"""
Este modulo tiene una funcion de suma.
"""


def add_integer(a, b=98):
    """
    Esta funcion suma dos numeros enteros.

    Args:
        a: primer agumento a sumar.
        b: segundo argumento a sumar.

    Returns:
        (a + b): la suma de dos enteros.

    Raises:
        TypeError: si a o b no son (int) y/o (float).
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return (a + b)
