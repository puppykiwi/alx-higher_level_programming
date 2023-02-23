#!/usr/bin/python3
'''Program that adds two variables'''


def add_integer(a, b=98):

    '''typecasts float to ints'''
    if type(int(a)) != int:
        raise TypeError("a must be an integer")
    elif type(int(b)) != int:
        raise TypeError("b must be an integer")
    else:
        return (int(a)+int(b))
