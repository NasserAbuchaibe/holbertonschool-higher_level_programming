#!/bin/bash
# Bash script
curl -sI -X OPTIONS "$1" | grep Allow | cut -d ' ' -f2-
