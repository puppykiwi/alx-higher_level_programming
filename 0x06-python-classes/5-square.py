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

    def my_print(self):
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print('#', end='')
            print()


if __name__ == "__main__":
    Square = __import__('5-square').Square

    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")
