#!/usr/bin/python3
""" POST an email
"""
import urllib.request
from sys import argv
import urllib.parse

if __name__ == "__main__":
    """ok
    """
    url = argv[1]
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode("utf-8"))
