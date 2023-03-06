#!/usr/bin/python3
'''creates a square class'''


class Square(__import__('7-base_geometry').BaseGeometry):
    def __init__(self, size):
        BaseGeometry.integer_validator("size", size)
        self.__size = size
    
    def area(self):
        return self.__size * self.__size