#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
    message = """Body response:
        - type: {}
        - content: {}
        - utf8 content: {}""".format(type(html), html, html.decode("utf-8"))
    print(message)
