#!/usr/bin/python3
"""
Este modulo captura los argumentos pasados.

lista (list): lista donde se guardaran los argumentos pasados.
"""

from sys import argv
from os.path import exists

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

lista = []
if exists("add_item.json"):
    lista = load_from_json_file("add_item.json")

for i in argv[1:]:
    lista.append(i)

save_to_json_file(lista, "add_item.json")
