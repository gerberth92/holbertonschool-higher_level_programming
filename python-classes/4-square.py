#!/usr/bin/python3
"""
Esta es una clase.
"""


class Square:
    """
    Esta es una clase de nombre square.

    Attributes:
        __size (int): es un atributo que no tiene que ser negativo.
    """

    def __init__(self, size=0):
        """
        Inicializando un metodo constructor.

        Args:
            __size (int): es un entero igual o mayor que 0.

        Raises:
            Exception: muestra un mesaje de error si size no es (int)
            o es menor que 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        funcion que retorna el area de un cuadrado
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """
        Captura el atributo size..

        Return:
            int: el valor de size.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Captura el atributo size.

        args:
            value (int): el nuevo valor de size.

        Raises:
            TypeError: si (value) no es un entero.
            ValueError: si (value) es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
