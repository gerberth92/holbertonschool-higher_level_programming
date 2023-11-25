#!/usr/bin/python3
"""
este modulo tiene una funcion.
"""
import json


def load_from_json_file(filename):
    """Esta funcion desserializa un archivo .json.

    Args:
        filename: es el archivo .json

    Returns:
        El objeto desserializado.
    """
    with open(filename, 'r') as archivo:
        return (json.load(archivo))
