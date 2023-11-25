#!/usr/bin/python3
"""
Este modulo tiene una funcion que lee.
"""


def read_file(filename=""):
    """
    Esta funcion abre, lee y cierra un archivo.

    Args:
        filename (txt): este es el archivo que se abrira.
    """
    with open(filename, 'r', encoding="utf-8") as archivo:
        contenido = archivo.read()
        print(contenido, end='')
