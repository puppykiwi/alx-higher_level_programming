#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
from urllib.request import urlopen as uopen

if __name__ == "__main__":
    with uopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('utf-8')),end="")
