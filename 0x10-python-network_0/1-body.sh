#!/bin/bash
# Send a GET request to the URL and display the body of the response for a 200 status code
response=$(curl -s -w "%{http_code}" -o response_body.txt "$1")
status_code=$(tail -c 3 <<< "$response")
if [ "$status_code" -eq 200 ]; then
    cat response_body.txt
fi
