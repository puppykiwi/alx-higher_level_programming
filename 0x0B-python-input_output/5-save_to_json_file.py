#!/usr/bin/python3
'''loads the JSON notation to a file'''
import json


def save_to_json_file(my_obj, filename):
    '''opens and writes the file'''
    with open(filename, 'w+') as f:
        return json.dump(my_obj, f)
