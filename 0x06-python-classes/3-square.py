#!/usr/bin/python3
'''create a class '''


class Square:
    '''inits 2 attributes'''
    def __init__(self, size=0):
        '''initiates the atr=t'''
        if type(size) != int:
            raise TypeError("size must be an integer.")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''this function returns the area'''
        return (self.__size * self.__size)
