#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    """ ok
    """
    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(r.text))
    print("\t- content: {}".format(r.text))
