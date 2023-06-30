#!/usr/bin/python3
'''handlimng http errors using requests package'''
from requests import get
from sys import argv
url = argv[1]

if __name__ == "__main__":
    with get(url) as response:
        if response.status_code >= 400:
            print('Error code: {}'.format(response.status_code))
        else:
            print(response.text)
