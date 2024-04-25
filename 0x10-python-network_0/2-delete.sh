#!/bin/bash
# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi
curl -s -X DELETE "$1"
