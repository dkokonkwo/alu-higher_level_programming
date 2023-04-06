#!/bin/bash
# sends POST request with JSON file to given URL and displays response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
