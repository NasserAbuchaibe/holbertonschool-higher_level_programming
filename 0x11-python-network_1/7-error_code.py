#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status
"""
import requests
from sys import argv


if __name__ == "__main__":
    """ ok
    """
    r = requests.get(argv[1])
    if r.status_code < 400:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
