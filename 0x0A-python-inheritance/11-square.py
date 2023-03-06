#!/usr/bin/python3
'''creates a square class'''


class Square(__import__('9-rectangle').Rectangle):
    '''forgot the class doc'''
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))


if __name__ == '__main__':
    s = Square(11)

    print(s)
    print(s.area())
