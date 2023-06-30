#!/usr/bin/python3
"""python api to fetch user json data"""
from requests import post
from sys import argv
url = "http://0.0.0.0:5000/search_user"

if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    data = {'q': q}
    with post(url, data) as response:
        try:
            json = response.json()
            if json:
                print("[{}] {}".format(json.get('id'), json.get('name')))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
