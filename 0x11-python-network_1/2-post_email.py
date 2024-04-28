#!/usr/bin/python3
"""
Sends a POST request to a URL with an email parameter and displays the body of the response.
"""

import urllib.request
import urllib.parse
import sys

def send_post_request(url, email):
    """
    Sends a POST request to the specified URL with the provided email parameter.
    
    Args:
        url (str): The URL to send the request to.
        email (str): The email parameter to include in the request.
    """
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    req = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
        sys.exit(1)
    
    url = sys.argv.get(1)
    email = sys.argv.get(2)
    send_post_request(url, email)

