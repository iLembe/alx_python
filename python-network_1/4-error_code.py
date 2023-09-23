"""
This script takes a URL as input, sends a request to the URL, displays the body of the response,
and prints an error message if the HTTP status code is greater than or equal to 400.

Usage: python script.py <URL>

You must have the 'requests' and 'sys' packages installed.

If the HTTP status code is an error (>= 400), it will print: Error code: followed by the status code.

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

        # Display the body of the response
        print(response.text)

        # Check if the HTTP status code is an error (>= 400)
        if response.status_code >= 400:
            print("Error code:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("Error:", e)
