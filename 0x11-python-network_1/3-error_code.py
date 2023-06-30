#!/usr/bin/python3
'''handling http errors'''
from urllib.request import urlopen as open
from urllib.error import HTTPError
from sys import argv
url = argv[1]

try:
    with open(url) as response:
        data = response.read().decode('utf-8')
        print(data)
except HTTPError as e:
    print('Error code: {}'.format(e.code))
