#!/usr/bin/python3
'''creating a student class'''


def class_to_json(obj):
    """
    returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization of
    an object
    """
    return obj.__dict__


class Student:
    '''defines a student class that has attrs'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''returns a dict whfndevf'''
        if attrs is None:
            return self.__dict__
        else:
            mdict = {}
            for i in attrs:
                if hasattr(self, i):
                    mdict[i] = self.__dict__[i]
            return mdict

    def reload_from_json(self, json):
        '''loads from a json dict with alot of docs'''
        self.__dict__.clear()
        for i in json:
            self.__dict__[i] = json[i]
