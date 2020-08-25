#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status
"""
import requests
from sys import argv


if __name__ == "__main__":
    """ ok
    """
    url = "https://api.github.com/repos/"
    repo_name = argv[1]
    own_name = argv[2]
    full_url = "{}{}/{}/commits".format(url, own_name, repo_name)
    r = requests.get(full_url)
    res = r.json()
    count = 0
    for d in res:
        commit = d.get('commit')
        author = commit.get('author')
        print("{}: {}".format(d.get('sha'), author.get('name')))
        count += 1
        if count == 10:
            break
