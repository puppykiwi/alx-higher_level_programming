#!/usr/bin/python3
'''loading objects'''
import json


def load_from_json_file(filename):
    '''generic comment'''
    with open(filename, 'r') as f:
        return json.load(f)
