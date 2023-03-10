#!/usr/bin/python3
'''loading from a json file'''
import json


def from_json_string(my_str):
    '''converts a string to an object'''
    return json.load(my_str)
