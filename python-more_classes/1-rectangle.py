#!/usr/bin/python3
"""
Esta es una clase que define un rectangulo.
"""


class Rectangle:
    """
    Esta funcion define un rectangulo y tiene dos argumentos.

    Args:
        width (int): arguento 1 que es un entero mayor que 0.
        height (int): argumento 2 que es un entero mayor que 0.

    Raises:
        TypeError: si width no es un entero.
        TypeError: si height no es un entero.
        ValueError: si width es menor que 0.
        ValueError: si height es menor que 0.
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
