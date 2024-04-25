#!/bin/bash
# Check if both URL and file arguments are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <URL> <filename>"
    exit 1
fi
if [ ! -f "$2" ]; then
    echo "File '$2' not found."
    exit 1
fi
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
