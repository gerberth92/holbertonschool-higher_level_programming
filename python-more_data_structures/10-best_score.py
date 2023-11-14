#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)

    new = 0
    for key, value in a_dictionary.items():
        if value > new:
            new = value
            name = key
    return (name)
