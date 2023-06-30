#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""
from urllib.request import urlopen as uopen
with uopen('https://intranet.hbtn.io/status') as response:
    html = response.read()

if __name__ == "__main__":
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('utf-8')))
