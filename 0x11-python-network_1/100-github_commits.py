#!/usr/bin/python3
"""
This script takes two arguments - github repository name, and owner name and
displays the commits and author in the form `<sha>: <author name>
"""

import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    repo_owner = sys.argv[2]
    url = f"https://api.github.com/repos/{repo_owner}/{repo}/commits"

    res = requests.get(url)
    results = res.json()
    try:
        for i in range(0, 10):
            sha = results[i].get('sha')
            author = results[i].get('commit').get('author').get('name')
            print("{}: {}".format(sha, author))
    except Exception:
        pass
