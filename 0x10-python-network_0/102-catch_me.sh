#!/bin/bash
# Send a PUT request with a custom header to the specified URL
curl -s -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
