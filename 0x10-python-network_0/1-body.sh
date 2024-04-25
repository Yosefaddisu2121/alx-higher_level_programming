#!/bin/bash
# Check if the URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi
response=$(curl -s -o /dev/null -w "%{size_download}" "$1")
curl -s -o response.tmp -w "%{http_code}" "$1" | {
    read status_code
    if [ "$status_code" = "200" ]; then
        cat response.tmp
    else
        echo "Error: Received status code $status_code"
    fi
}
rm response.tmp
