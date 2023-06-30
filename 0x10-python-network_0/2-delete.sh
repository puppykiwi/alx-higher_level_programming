#!/bin/bash
# send a delete request
response=$(curl -sL -X DELETE "$1");echo "$response"; body=${response::-3}; echo "$body"
