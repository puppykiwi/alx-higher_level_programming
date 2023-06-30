#!/bin/bash
# send a post request with variables set and display body of response
curl -sX post -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD" "$1"
