#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv
    c = len(argv)
    sum = 0

    if c == 1:
        print("0")

    if c > 1:
        for i in range(1, c):
            d = int(argv[i])
        
            sum = sum + d

        print(sum)
