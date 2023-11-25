#!/usr/bin/python3
"""
Este modulo importaq json y tiene una funcion que deserializa.
"""
import json


def from_json_string(my_str):
    """
    Esta funcion retorna una deserializacion.

    Args:
        my_str: objeto a deserializar.
    """
    return (json.loads(my_str))
