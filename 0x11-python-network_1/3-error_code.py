#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the response, handling HTTP errors.
"""

import urllib.request
import urllib.error
import sys
url = f'https://api.github.com/users{Yosefaddisu2121}'
if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")

