#!/usr/bin/python3
'''creates a class'''


class Rectangle(__import__('7-base_geometry').BaseGeometry):
    '''instantiates the class'''
    def __init__(self, width, height):
        '''initializes these private attr'''
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def integer_validator(self, name, value):
        '''validates input'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
