#!/usr/bin/python3

def print_list_integer(my_list=[]):
    
    c = len(my_list)
    for i in range(c):
        print("{}".format(my_list[i]))


if __name__ == "__main__":
    print_list_integer()
