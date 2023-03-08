#!/usr/bin/python3
'''appendign toa file'''


def append_write(filename="", text=""):
    '''opens a nd aooends text to a file'''
    with open(filename, 'w') as f:
        return f.write(text)
