#!/bin/bash
# Check if the URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi
email="test@gmail.com"
subject="I will always be here for PLD"
curl -s -X POST -d "email=$email&subject=$subject" "$1"