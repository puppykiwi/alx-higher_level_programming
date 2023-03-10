#!/usr/bin/python3
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
'''loading lists of args'''

def additem():
    '''just a simple function'''
    list = []

    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            list.append(sys.argv[i])

    save_to_json_file(list, 'add_item.json')

additem()