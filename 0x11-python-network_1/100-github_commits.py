#!/usr/bin/python3
"""lists commits (from the most recent to oldest) of a repository"""
from requests import get
from sys import argv

if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    with get(url) as response:
        for commit in response.json()[:10]:
            print('{}: {}'.format(commit.get('sha'),
                                  commit.get('commit').get('author').get('name')))
