#!/usr/bin/python3
"""
Este modulo tienen una clase que define una base geometrica.
"""


class BaseGeometry:
    """
    Esta clase define una base geometrica.
    """
    def area(self):
        """
        Esta funcion levanta una excepcion.

        Raises:
            Exception: el area no esta implementada.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Esta funcion valida el formato de (value).

        Args:
            name (str): arguento de tipo string.
            value (int): argumento de tipo int.

        Raises:
            TypeError: si es diferente de (int).
            ValuError: si es menor o igual a 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
