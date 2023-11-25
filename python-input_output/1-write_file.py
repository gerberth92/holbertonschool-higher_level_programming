#!/usr/bin/python3
"""
Este modulo tiene una funcion que crea y escribe texto.
"""


def write_file(filename="", text=""):
    """
    Esta funcion abre un archivo.

    Args:
        filename (.txt): archivo a crear o sobreescribe.
        text (str): mensaje a escribir.

    Returns:
        Retorna el numero de letras escritas.
    """
    with open(filename, 'w', encoding="utf-8") as archivo:
        return (archivo.write(text))
