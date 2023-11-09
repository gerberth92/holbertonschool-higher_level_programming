#!/usr/bin/python3

from sys import argv

argumento = argv
c = len(argv)

if c == 1:
    print(f"{c-1} arguments.")

if c == 2:
    print("1 argument:")

if c > 2:
    print(f"{c-1} arguments:")

for i in range(1, c):
    print(f"{i}: {argv[i]}")
