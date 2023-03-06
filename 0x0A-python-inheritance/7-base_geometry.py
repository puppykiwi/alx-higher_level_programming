#!/usr/bin/python3
'''creates a class'''


class BaseGeometry:
    '''instantiates the class'''
    def area(self):
        '''raises an error'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validates input'''
        if type(value) is int:
            if int(value) <= 0:
                raise ValueError(name, " must be greater than 0")
        else:
            raise TypeError(name, " must be an integer")
