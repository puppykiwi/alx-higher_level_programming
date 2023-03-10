#!/usr/bin/python3
import json
import sys
'''loading lists of args'''

def additem():
    '''just a simple function'''
    list = []

    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            list.append(sys.argv[i])

    with open("add_item.json", 'w+') as f:
        json.dump(list, f)

additem()