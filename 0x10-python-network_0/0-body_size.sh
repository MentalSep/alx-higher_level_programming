#!/bin/bash
# displays the size of the body of the response of a URL
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
