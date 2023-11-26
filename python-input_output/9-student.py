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

    def to_json(self):
        """
        Esta funcion retorna un diccionario con los atributos.
        """
        return (self.__dic__.copy())
