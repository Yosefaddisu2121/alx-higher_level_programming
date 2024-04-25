#!/bin/bash
# This script takes a URL as input and displays all HTTP methods the server will accept

# Check if correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 URL"
    exit 1
fi

# Retrieve HTTP methods supported by the server
curl -s -i -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-

