#!/bin/bash
# This script takes a URL as input and displays all HTTP methods the server will accept
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 URL"
    exit 1
fi
curl -s -i -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
