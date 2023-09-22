"""
This script takes a URL as input, sends a request to the URL using the 'requests' package,
and displays the value of the 'X-Request-Id' variable in the response header.

Usage: python script.py <URL>

You must have the 'requests' and 'sys' packages installed.

The value of the 'X-Request-Id' variable is different for each request.

Note: No argument validation is performed in this script.
"""

import requests
import sys

if __name__ == "__main__":
    # Check if a URL is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors

        # Check if the 'X-Request-Id' header is present in the response
        if 'X-Request-Id' in response.headers:
            request_id = response.headers['X-Request-Id']
            print(request_id)
        else:
            print("X-Request-Id header not found in the response")

    except requests.exceptions.RequestException as e:
        print("Error:", e)
