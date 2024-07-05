#!/usr/bin/python3
'''Creates a rectangle class'''
from models.base import Base


class Rectangle(Base):
    '''The rectangle class'''
    def __init__(self, height, width, x=0, y=0, id=None):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        '''class initializer'''
        super().__init__(id)
        self.__height = height
        self.__width = width
        self.__x = x
        self.__y = y

    @property
    def height(self):
        '''This is an attr height getter'''
        return self.__height

    @property
    def width(self):
        '''This is an attr width getter'''
        return self.__width

    @property
    def x(self):
        '''This is an attr y getter'''
        return self.__x

    @property
    def y(self):
        '''This is an attr x getter'''
        return self.__y

    @height.setter
    def height(self, val):
        '''THis is a height setter'''
        self.__height = val

    @width.setter
    def width(self, val):
        '''THis is a width setter'''
        self.__width = val

    @x.setter
    def x(self, val):
        '''THis is a x setter'''
        self.__x = val

    @y.setter
    def y(self, val):
        '''THis is a y setter'''
        self.__y = val


if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 3, 0, 0, 12)
    print(r3.id)
    print(r3.area())
