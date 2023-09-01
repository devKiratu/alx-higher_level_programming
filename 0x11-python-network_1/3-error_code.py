#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays the body
of the response (decoded in utf-8). Also handles errors gracefully
"""

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import sys

if __name__ == "__main__":
    req = Request(sys.argv[1])
    try:
        with urlopen(req) as response:
            body = response.read()
            print(body.decode("utf-8"))
    except HTTPError as e:
        print("Error code:", e.code)
    except URLError as e:
        print("Error code:", e.reason)
