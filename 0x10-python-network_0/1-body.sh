#!/bin/bash
# takes in a URL, send a GET request to the URL
curl -s -L -X get "$1"
