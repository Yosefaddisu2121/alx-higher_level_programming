#!/bin/bash
# Send a GET request to the URL and display the body of the response for a 200 status code
response=$(curl -s -w "%{http_code}" -o response_body.txt "$1")

# Extract the status code from the response
status_code=$(tail -c 3 <<< "$response")

# If the status code is 200, display the body of the response
if [ "$status_code" -eq 200 ]; then
    cat response_body.txt
fi
