#!/usr/bin/python3
'''creates a class'''


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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer.")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


if __name__ == "__main__":
    Square = __import__('4-square').Square

    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)
