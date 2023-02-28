#!/usr/bin/python3


def lookup(obj):
    '''returns a list of attributes'''
    list=[]
    list.append(dir(obj))
    return list
