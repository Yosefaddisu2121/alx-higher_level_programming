#!/bin/bash
# This script sends a POST request to the specified URL with email and subject variables and displays the response body
curl -s -X POST -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
