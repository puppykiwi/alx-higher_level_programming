#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
from requests import get

if __name__ == "__main__":
    with get('https://alx-intranet.hbtn.io/status') as response:
        html = response.text
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
