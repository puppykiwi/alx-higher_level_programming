#!/usr/bin/python3
'''duplicate of 2?'''


def inherits_from(obj, a_class):
    '''checks whether an object inherits from argv[1]'''
    return isinstance(obj, a_class) if type(obj) is not a_class else False


if __name__ == "__main__":
    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))
