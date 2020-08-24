#!/usr/bin/python3
""" Response header value
"""
import urllib.request
from sys import argv


if __name__ == __main__:
    """ok
    """
    with urllib.request.urlopen(argv[1]) as response:
        info_head = response.info()
        print(info_head[X-Request-Id])
