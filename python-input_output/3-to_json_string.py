#!/usr/bin/python3
"""
Este modulo importa json, y tiene una funcion.
"""


import json


def to_json_string(my_obj):
    """
    Esta funcion serializa.

    Args:
        my_objet: objeto a serializar.

    Return:
        Retorna una serializacion.
    """
    return (json.dumps(my_obj))
