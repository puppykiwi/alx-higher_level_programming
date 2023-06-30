#!/usr/bin/python3
'''accessing github user id using requests package'''
from requests import get
from sys import argv

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = argv[1]
    password = argv[2]
    with get(url, auth=(username, password)) as response:
        print(response.json().get('id'))
