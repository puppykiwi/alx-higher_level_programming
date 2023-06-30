#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status using requests package"""
from requests import get
from sys import argv
if __name__ == "__main__":
    url = argv[1]
    with get(url) as response:
        print(response.headers.get('X-Request-Id'))
