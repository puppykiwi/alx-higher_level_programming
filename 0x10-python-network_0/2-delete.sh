#!/bin/bash
# send a delete request
response=$(curl -sL -X DELETE "$1"); body=$response; echo "$body"
