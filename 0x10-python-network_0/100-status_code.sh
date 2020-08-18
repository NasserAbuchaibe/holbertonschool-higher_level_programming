#!/bin/bash
# Bash script
curl -w "%{http_code}" -so /dev/null "$1"
