#!/usr/bin/python3
"""
Fetches the body of a URL using urllib
"""
import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        data = response.read().decode('utf-8')
        print("Body response:")
        print("\t- type:", type(data))
        print("\t- content:", data)

