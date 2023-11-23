#!/usr/bin/python3
"""
Este modulo importa una funcion y define una clase rectangle con herencia.
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Esta funcion hereda de BaseGeometry y tiene un constructor.
    """
    def __init__(self, width, height):
        """
        Iniciando el constructor que acepta dos argumentos.

        Args:
            width (int): argumento de tipo int
            height (int): argumento de tipo int
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
