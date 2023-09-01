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
        res.raise_for_status()
        result = res.json()
        print(type(result))
    except requests.exceptions.HTTPError as e:
        if res.status_code == 204:
            print("No result")
    except requests.exceptions.JSONDecodeError as e:
        print("Not a valid JSON")
    except requests.exceptions.RequestException as e:
        pass
