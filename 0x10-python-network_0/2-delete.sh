#!/bin/bash
# send a delete request
response=$(curl -s -L -X DELETE "$1"); echo "$response"
