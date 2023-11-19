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

    def __init__(self, size=0, position=(0, 0)):
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
            self.__position = position

    def area(self):
        """
        funcion que retorna el area de un cuadrado
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """
        Captura el atributo size.

        Return:
            int: el valor de size.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Captura el atributo size.

        Args:
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

    @property
    def position(self):
        """
        Captura el atributo position.

        Return:
            tuple: una tupla de dos enteros positivos
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Captura el atributo position.

        Args:
            value (tuple, int): captura el valor de (position) que es
            una tupla de dos enteros.

        Raises:
            TypeErro: si (value) no es una tupla, entero o es si tiene
            mas o menos de dos elementos.
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Imprime "#" con el tamaño del cuadrado, si (__size) es
        igual a 0, imprime una linea en blanco.
        Imprime una linea en blanco de acuerdo al valor
        del indice 0 de la tupla.
        Imprime una espacio en blanco de acuerdo al valor
        del indice 1 de la tupla.
        """
        if self.__size == 0:
            print()
        else:
            for a in range(self.__position[1]):
                print()

            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end='')
                for a in range(self.__size):
                    print("#", end='')
                print()
