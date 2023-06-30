#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
from requests import get
with get('https://alx-intranet.hbtn.io/status') as response:
    html = response.text

if __name__ == "__main__":
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
