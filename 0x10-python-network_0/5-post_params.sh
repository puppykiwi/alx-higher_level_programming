#!/bin/bash
# send a post request with variables set and display body of response
curl -sX POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
