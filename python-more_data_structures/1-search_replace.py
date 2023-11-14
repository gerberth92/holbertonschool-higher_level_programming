#!/usr/bin/python3

def search_replace(my_list, search, replace):
    lista = my_list.copy()

    for i in range(len(lista)):
        if lista[i] == search:
            lista[i] = replace
    return (lista)
