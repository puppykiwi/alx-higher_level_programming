#!/usr/bin/python3
'''writing to a file'''


def write_file(filename="", text=""):
    with open(filename, 'r+', encodeing="utf-8") as f:
        return f.write(text)
