#!/bin/bash
# makes a request and causes the server to respond with a message
curl -sLX PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
