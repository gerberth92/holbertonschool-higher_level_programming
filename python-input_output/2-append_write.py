#!/usr/bin/python3
"""
Este modulo tiene una funcion que agrega una string.
"""

def append_write(filename="", text=""):
    """
    Esta funcion agrega una string al final del archivo.

    Args:
        filename (.txt): archivo de texto
        text (str): string

    Returns:
        Cantidad de letras agregadas.
    """
    with open(filename, 'a', encoding="utf-8") as archivo:
        return (archivo.write(text))
