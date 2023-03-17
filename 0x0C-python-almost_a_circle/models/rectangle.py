#!/usr/bin/python3
'''Creates a rectangle class'''
from base import Base


class Rectangle(Base):
    '''The rectangle class'''
    def __init__(self, height, width, x=0, y=0, id=None):
        '''class initializer'''
        super().__init__(id)
        self.__height = height
        self.__width = width
        self.__x = x
        self.__y = y

    @property
    '''This is an attr getter'''
    def height(self):
        return self.__height

    @property
    '''This is an attr getter'''
    def width(self):
        return self.__width

    @property
    '''This is an attr getter'''
    def x(self):
        return self.__x

    @property
    '''This is an attr getter'''
    def y(self):
        return self.__y

    @height.setter
    '''THis is a setter'''
    def height(self, val):
        self.__height = val

    @width.setter
    '''THis is a setter'''
    def width(self, val):
        self.__width = val
        '''This is an attr setter'''

    @x.setter
    '''THis is a setter'''
    def x(self, val):
        self.__x = val

    @y.setter
    '''THis is a setter'''
    def y(self, val):
        self.__y = val


if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)
