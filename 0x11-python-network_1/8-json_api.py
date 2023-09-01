#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys


if __name__ == "__main__":
    search_param = ""
    if len(sys.argv) >= 2:
        search_param = sys.argv[1]
    values = {'q': search_param}
    try:
        res = requests.post('http://0.0.0.0:5000/search_user', data=values)
        result = res.json()
        if len(result) == 0:
            print("No result")
        else:
            print("[{}] {}".format(result.get('id'), result.get('name')))
    except ValueError as e:
        print("Not a valid JSON")
    except requests.exceptions.RequestException as e:
        pass
