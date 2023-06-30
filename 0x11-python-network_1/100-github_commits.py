#!/usr/bin/python3
"""lists commits (from the most recent to oldest) of a repository"""
from requests import get
from sys import argv

if __name__ == "__main__":
    repository_name = argv[1]
    owner_name = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner_name, repository_name)
    with get(url) as response:
        for commit in response.json()[:10]:
            print('{}: {}'.format(commit.get('sha'),commit.get('commit').get('author').get('name')))
