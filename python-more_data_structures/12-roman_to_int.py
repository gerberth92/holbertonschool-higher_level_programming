#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return (0)

    romano = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    suma = 0

    for i in range(len(roman_string)):
        if i > 0 and romano[roman_string[i]] > romano[roman_string[i - 1]]:
            suma += romano[roman_string[i]] - 2 * romano[roman_string[i - 1]]
        else:
            suma += romano[roman_string[i]]
    return (suma)
