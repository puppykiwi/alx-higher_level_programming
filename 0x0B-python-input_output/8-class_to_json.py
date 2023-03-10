#!/usr/bin/python3
'''creates a dict'''
import json


def class_to_json(obj):
    '''converts a class dict'''
    return obj.__dict__
