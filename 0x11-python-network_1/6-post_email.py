#!/usr/bin/python3
""" Response header value
"""
import requests
from sys import argv


if __name__ == "__main__":
    """ok
    """
    url = argv[1]
    data = {'email': argv[2]}
    r = requests.post(url, data=data)
    print(r.text)
