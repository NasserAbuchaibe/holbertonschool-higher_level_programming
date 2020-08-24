#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    """ ok
    """
    try:
        with urllib.request.urlopen(argv[1]) as response:
            html = response.read()
            print(html.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
