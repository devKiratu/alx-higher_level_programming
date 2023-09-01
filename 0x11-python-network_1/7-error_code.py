#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays the body
of the response. Also handles errors and displays errors gracefully
"""

import requests
import sys

if __name__ == "__main__":
    try:
        res = requests.get(sys.argv[1])
        res.raise_for_status()
        print(res.text)
    except requests.exceptions.RequestException as e:
        if res.status_code >= 400:
            print("Error code:", res.status_code)
