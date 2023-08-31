#!/bin/bash
# This script takes in a URL, sends a GET request to the URL, and displays the body of a 200 response
curl -sIL -o /dev/null "$1" -w "%{http_code}" | grep -q 200 && curl -sL "$1" 
