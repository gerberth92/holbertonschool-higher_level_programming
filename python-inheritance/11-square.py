#!/usr/bin/python3
"""
Este modulo importa una clase e inicia una clase.
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Esta clase hereda de Rectangle, define un cuadrado e inicia un constructor.
    """
    def __init__(self, size):
        """
        Se inicia un constructor.

        Args:
            size (int): argumento de tipo int.

        Llama a un metodo de la superclase
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """
        Retorna el area del cuadrado llamando a una funcion de la superclase.
        """
        return (super().area())

    def __str__(self):
        """
        Esta funcion retorna un mensaje.
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))
