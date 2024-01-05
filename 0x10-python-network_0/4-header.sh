#!/bin/bash
# sends a GET request with a header to the URL passed, and displays the body of the response
curl -sH "X-School-User-Id: 98" "$1"
