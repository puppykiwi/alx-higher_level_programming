#!/bin/bash
# Takes in a URL, sends a request to that URL, and displays the body of the response only if the status code is 200
# Function to send GET request and display response body
send_get_request() {
  url=$1
  response=$(curl -s -w "%{http_code}" "$url")
  status_code=${response: -3}  # Extract last 3 characters (status code)
  body=${response::-3}  # Extract response body (excluding status code)

  if [[ $status_code -eq 200 ]]; then
    echo "Response Body:"
    echo "$body"
  else
    echo "Error: Status code $status_code received"
  fi
}

# Check if URL argument is provided
if [[ $# -eq 0 ]]; then
  echo "Error: URL argument is required"
  exit 1
fi

# Extract URL from the first argument
url=$1

# Call the function to send the GET request and display the response
send_get_request "$url"
