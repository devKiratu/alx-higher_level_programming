#!/usr/bin/python3
"""
This script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the
response. Uses requests package
"""

import requests
import sys

if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    res = requests.post(sys.argv[1], data=values)
    print(res.text)
