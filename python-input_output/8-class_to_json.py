#!/usr/bin/python3
"""
Este modulo tiene una funcion.
"""


def class_to_json(obj):
    """
    Esta funcion devuelve una descripcion.
    """
    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
