#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    num = len(argv) - 1
    i = 1
    Total = 0
    while i <= num:
        Total += int(argv[i])
        i += 1

    print(Total)
