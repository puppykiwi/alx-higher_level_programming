#!/bin/bash
# send a get request with header variable set and display body of response
curl -s -H "X-School-User-Id: 98" "$1"
