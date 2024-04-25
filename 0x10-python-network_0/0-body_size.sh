#!/bin/bash
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi
response=$(curl -s -o response.tmp -w "%{size_download}" "$1")
if [ $? -ne 0 ]; then
    echo "Error: Unable to fetch URL $1"
    exit 1
fi
echo "Size of the response body: $response bytes"
rm response.tmp
