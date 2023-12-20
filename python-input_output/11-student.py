#!/usr/bin/python3
"""
Este modulo tiene una clase.
"""


class Student:
    """
    Esta clase define un estudiante.
    """
    def __init__(self, first_name, last_name, age):
        """
        Inicializando el constructor.

        Args:
            first_name: nombre
            last_name: apellido
            age: edad
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Esta funcion retorna un diccionario con los atributos.
        """
        if isinstance(attrs, list):
            new = {}
            for i in attrs:
                if hasattr(self, i):
                    new[i] = getattr(self, i)
            return (new)

        else:
            return (self.__dict__.copy())

    def reload_from_json(self, json):
        """
        Esta funcion reemplaza el valor de los atributos.

        Args:
            json: es un diccionario.
        """
        for clave, valor in json.items():
            setattr(self, clave, valor)
