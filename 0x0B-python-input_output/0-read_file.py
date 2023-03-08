#!/usr/bin/python3
'''Reading and printing a file'''


def read_file(filename=""):
    '''opening and reading'''
    with open(filename, encoding="utf-8") as f:
        f.readlines()
