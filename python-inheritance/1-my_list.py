#!/usr/bin/python3
"""
Este modulo tiene una clase que hereda de list.
"""
class MyList(list):
    """
    Esta clase hereda de list.

    Args:
        list: clase lista.
    """
    def print_sorted(self):
        """
        Esta funcion imprime una lista ordenada.
        """
        copia = self.copy()
        copia.sort()
        print(copia)
