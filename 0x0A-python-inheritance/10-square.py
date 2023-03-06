#!/usr/bin/python3
'''creates a square class'''


class Square(__import__('9-rectangle').Rectangle):
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size


if __name__ == '__main__':
    s = Square(13)

    print(s)
    print(s.area())
