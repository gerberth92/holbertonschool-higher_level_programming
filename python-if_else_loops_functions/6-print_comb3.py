#!/usr/bin/python3

for i in range(0, 10):
    for a in range(0, 10):
        if i != a and i < a and i < 9:
            if i == 8 and a == 9:
                print("{:d}{:d}".format(i, a))
            else:
                print("{:d}{:d}, ".format(i, a), end='')
