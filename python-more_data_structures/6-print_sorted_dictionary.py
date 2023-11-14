#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    lista = sorted(list(a_dictionary))
    for i in lista:
        print("{}: {}".format(i, a_dictionary.get(i)))
