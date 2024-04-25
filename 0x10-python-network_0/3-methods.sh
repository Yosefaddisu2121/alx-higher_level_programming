#!/bin/bash
# Check if the URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi
curl -s -X OPTIONS -i "$1" | grep -i "Allow" | cut -d ':' -f 2- | tr -d '[:space:]'
