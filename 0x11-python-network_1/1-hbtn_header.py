#!/usr/bin/python3
'''reading http headers'''
from urllib.request import urlopen as open
from sys import argv
url = argv[1]
with open(url) as response:
    print(response.headers.get('X-Request-Id'))
