#!/bin/bash
# sends GET request to given URL, with key-value, and displays body of response
curl -sX GET -H "X-HolbertonSchool-User-Id:98" "$1"
