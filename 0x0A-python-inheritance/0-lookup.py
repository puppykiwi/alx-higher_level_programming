#!/usr/bin/python3
'''creates a class'''

def lookup(obj):
    '''returns a list of attributes'''
    list=[]
    list.append(dir(obj))
    return list
