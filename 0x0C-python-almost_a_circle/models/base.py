#!/usr/bin/python3
'''Creates a base class'''


class Base:
    '''This will be the base class for the project'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''class initiator'''
        if id is not None:
            self.id = id
        else:
            self.__nb_objects = self.__nb_objects + 1
            self.id = self.__nb_objects


if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)
