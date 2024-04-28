#!/usr/bin/python3
"""
Fetches the body of a URL using the requests package.
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.text
        print("Body response:")
        print("\t- type:", type(data))
        print("\t- content:", data)
    else:
        print(f"Error code: {response.status_code}")

