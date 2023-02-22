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


if __name__ == "__main__":
    my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))
