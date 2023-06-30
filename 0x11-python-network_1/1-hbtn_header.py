#!/usr/bin/python3
'''reading http headers using urllib package'''
from urllib.request import urlopen as open
from sys import argv
url = argv[1]

if __name__ == "__main__":
    with open(url) as response:
        print(response.headers.get('X-Request-Id'))
