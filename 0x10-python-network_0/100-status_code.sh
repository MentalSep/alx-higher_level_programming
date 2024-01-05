#!/bin/bash
# displays only the status code of the response of a URL
curl -sw "%{http_code}" "$1" -o /dev/null
