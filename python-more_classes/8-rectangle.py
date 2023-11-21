#!/usr/bin/python3
"""
Esta es una clase que define un rectangulo.
"""


class Rectangle:
    """
    Esta funcion define un rectangulo y tiene dos argumentos.

    Attributes:
        __width (int): atributo privado.
        __height (int): atributo privado.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Iniciando un metodo constructor.

        Args:
            width (int): es un entero mayor o igual que 0.
            height (int): es un entero mayor o igual que 0.
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Metodo que captura width.

        Returns:
            Retorna el valor de width.
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Metodo que cambia el valor de width.

        Args:
            value (int): es de tipo entero mayor o igual a 0.

        Raises:
            TypeError: si width no es un entero.
            ValueError: si width es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Metodo que captura height.

        Returns:
            Retorna el valor de height.
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Metodo que asigna el valor a height.

        Args:
            value (int): es de tipo entero mayor o igual que 0.

        Raises:
            TypeError: si height no es un entero.
            ValueError: si height es menor que 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """
        Esta funcion calcula el area de un rectangulo.

        Returns:
            Retorna el area del rectangulo.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Esta funcion calcula el perimetro de un rectangulo.

        Return:
            Retorna el perimetro de un rectangulo.
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """
        Funcion que imprime un rectangulo con "#".

        Returns:
            Cadena vacia si width o height es igual a 0.
            Una cadena que representa el rectangulo.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        cadena = ""
        for h in range(self.__height):
            cadena += str(self.print_symbol) * self.__width + '\n'
        return (cadena[:-1])

    def __repr__(self):
        """Funcion que devuelve una representacion del objeto.

        Returns:
            Retorna una cadena que represena el objeto.
        """
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """
        Esta funcion imprime un mensaje cuando se elimina un objeto.
        """
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """
        Esta funcion calcula y retorna el area de dos rectangulos.

        Args:
            rect_1 (Rectangle.objeto): es una instancia de Rectangle.
            rect_2 (Rectangle.objeto): es una instancia de Rectangle.

        Raises:
            TypeError: si rect_1 o rect_2 no son una instancia de Rectangle.

        Returns:
            Retorna la instancia con el area mas grande.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area1 = rect_1.__width * rect_1.__height
        area2 = rect_2.__width * rect_2.__height

        if area1 == area2:
            return (rect_1)
        if area1 > area2:
            return (rect_1)
        else:
            return (rect_2)
