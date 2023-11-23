#!/usr/bin/python3
"""
Este modulo tiene una funcion que verifica la clase.
"""


def is_kind_of_class(obj, a_class):
    """
    Esta valida si (obj) es una instancia de (a_class).

    Args:
        obj (object): objeto a verificar clase.
        a_class (class): tipo de clase a verificar.

    Returns:
        Retorna True si (obj) es una instancia de (a_class).
    """
    return (isinstance(obj, a_class))
