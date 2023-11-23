#!/usr/bin/python3
"""
Este modulo tiene una funcion que verifica si es una instancia.
"""


def inherits_from(obj, a_class):
    """
    Esta funcion verifica si es una instancia o type.

    Args:
        obj (object): objeto a verificar.
        a_class (class): clase con la cual verificar.

    Returns:
        Retorna False si es de typo a_class.
        Retorna True si es una instancia de a_class.
    """
    if type(obj) is a_class:
        return (False)
    return (isinstance(obj, a_class))
