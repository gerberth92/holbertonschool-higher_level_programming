#!/usr/bin/python3
"""
Este modulo tiene una funcion.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Esta funcion escribe y serializa.
    """
    with open(filename, 'w', encoding="utf-8") as archivo:
        return (archivo.write(json.dumps(my_obj)))
