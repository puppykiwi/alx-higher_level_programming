#!/usr/bin/python3
'''creates a class'''


class Rectangle:
    '''creates a rectangle class'''
    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("value must be an integer")
        elif value < 0:
            raise ValueError("value must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("value must be an integer")
        elif value < 0:
            raise ValueError("value must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        str1 = ""
        if self.__width == 0 or self.__height == 0:
            return (str1)
        for i in range(0, self.__height):
            for j in range(self.__width):
                str1 += "#"
            if i is not (self.__height - 1):
                str1 += '\n'
        return (str1)
    '''
    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            str1=''
        else:
            for i in range(0, self.height()):
                for _ in range(self.width()):
                    str1+='#'
                str1+='\n'
        return str1
    '''
