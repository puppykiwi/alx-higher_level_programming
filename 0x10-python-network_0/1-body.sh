#!/bin/bash
# Takes in a URL, sends a request to that URL, and displays the body of the response only if the status code is 200
response=$(curl -sL -w "%{http_code}" "$1"); status_code=${response: -3}; body=${response::-3}; [[ $status_code -eq 200 ]] && echo "$body"
