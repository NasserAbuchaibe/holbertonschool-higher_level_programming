#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status
"""
import requests
from sys import argv


if __name__ == "__main__":
    """ ok
    """
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) < 2:
        letter = ""
    else:
        letter = argv[1]
    data = {'q': letter}
    r = requests.post(url, data)

    try:
        file_json = r.json()
        if file_json:
            print("[{}] {}".format(file_json['id'], file_json['name']))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
