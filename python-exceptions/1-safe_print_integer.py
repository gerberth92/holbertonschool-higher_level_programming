#!/usr/bin/python3

def safe_print_integer(value):
    try:
        if isinstance(value, str):
            return (False)
        print(value)
        return(True)
    except TypeError:
        return (False)
