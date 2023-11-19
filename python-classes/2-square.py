#!/usr/bin/python3
"""
Esta es una clase.
"""


class Square:
    """
    Esta es una clase de nombre square.

    Attributes:
        __size(int): es un atributo que no tiene que ser negativo.
    """

    def __init__(self, size=0):
        """
        Inicializando un metodo constructor.

        args:
            __size(int): es un entero igual o mayor que 0.

        Raises:
            Exception: muestra un mesaje de error si size no es (int) o es menor que 0.
        """
        try:
            if type(size) is not int:
                raise Exception("size must be an integer")
            elif size < 0:
                raise Exception("size must be >= 0")
            else:
                self.__size = size

        except Exception as error:
            print(error)
