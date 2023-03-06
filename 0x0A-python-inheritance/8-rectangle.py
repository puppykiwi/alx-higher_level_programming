#!/usr/bin/python3
'''creates a class'''


class BaseGeometry:
    '''instantiates the class'''
    def __init__(self, width, height):
        '''initializes these private attr'''
        if type(width) != int:
            raise TypeError("{} must be an integer".format(width))
        if width <= 0:
            raise ValueError("{} must be greater than 0".format(width))
        self.__width = width

        if type(height) != int:
            raise TypeError("{} must be an integer".format(height))
        if height <= 0:
            raise ValueError("{} must be greater than 0".format(height))
        self.__height = height

    def area(self):
        '''raises an error'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validates input'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
