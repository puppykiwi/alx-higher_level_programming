#!/usr/bin/python3
"""reading http headers using urllib package"""
from urllib.request import urlopen as open
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    with open(url) as response:
        print(response.headers.get('X-Request-Id'))
