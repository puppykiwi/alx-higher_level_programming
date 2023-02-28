#!/usr/bin/python3
'''creates a class'''

def lookup(obj):
    '''returns a list of attributes'''
    list=[]
    list.append(obj.__dict__)
    return list


if __name__ == "__main__":
    class MyClass1(object):
        pass

    class MyClass2(object):
        my_attr1 = 3
        def my_meth(self):
            pass

    print(lookup(MyClass1))
    print(lookup(MyClass2))