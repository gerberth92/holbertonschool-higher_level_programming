#!/usr/bin/python3
"""
Este modulo tiene una funcion que lista los metodos y atributos.
"""


def lookup(obj):
    """
    Esta funcion lista los metodos y atributos.

    Args:
        obj (object): objeto a listar atributos y metodos.

    Returns:
        Una lista con todos los metodos y atributos.
    """
    return (list(dir(obj)))
