#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status using requests package"""
from requests import get
from sys import argv
url = argv[1]

if __name__ == "__main__":
    with get(url) as response:
        print(response.headers.get('X-Request-Id'))
