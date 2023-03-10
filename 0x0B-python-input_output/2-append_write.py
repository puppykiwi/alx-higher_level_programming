#!/usr/bin/python3
'''appendign toa file'''


def append_write(filename="", text=""):
    '''opens a nd aooends text to a file'''
    with open(filename, 'a+') as f:
        return f.write(text)
