#!/usr/bin/python3
""" Response header value
"""
import requests
from sys import argv


if __name__ == "__main__":
    """ok
    """
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
