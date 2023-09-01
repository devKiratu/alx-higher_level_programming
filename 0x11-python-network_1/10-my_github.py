#!/usr/bin/python3
"""
This script takes your GitHub credentials (username and password) and uses
the GitHub API to display your id
"""

import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == "__main__":
    uname = sys.argv[1]
    pat = sys.argv[2]
    url = "https://api.github.com/user"
    headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28"
            }
    auth = HTTPBasicAuth(uname, pat)
    res = requests.get(url, headers=headers, auth=auth)
    print(res.json().get('id'))
