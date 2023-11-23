#!/usr/bin/python3
"""
Este modulo tiene una funcion que verifica el tipo de clase.
"""


def is_same_class(obj, a_class):
    """
    Esta funcion retorna True si (obj) es del mismo tipo de clase de (a_class).
    """
    return (type(obj) is a_class)
