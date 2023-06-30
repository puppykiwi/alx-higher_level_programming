#!/usr/bin/python3
'''sends a POST request to the passed URL with the email as a parameter'''
from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data = parse.urlencode({'email': email}).encode()
    with request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
