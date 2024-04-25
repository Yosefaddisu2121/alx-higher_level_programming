#!/bin/bash
# This script sends a GET request to the specified URL with X-School-User-Id header and displays the response body
curl -s -H "X-School-User-Id: 98" "$1"
