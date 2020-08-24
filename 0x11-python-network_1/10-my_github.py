#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status
"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    """ ok
    """
    url = "https://api.github.com/users/"
    usr = argv[1]
    passw = argv[2]
    r = requests.get("{}{}".format(url, usr), auth=(usr, passw))
    print(r.json().get('id'))
