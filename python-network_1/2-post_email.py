"""
This script takes a URL and an email address as input, sends a POST request to the URL with the email as a parameter, and displays the body of the response.

Usage: python script.py <URL> <email>

You must have the 'requests' and 'sys' packages installed.

The 'email' parameter is sent in the POST request to the specified URL.

Note: No argument validation is performed in this script.
"""

import requests
import sys

if __name__ == "__main__":
    # Check if both a URL and an email address are provided as command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary with the 'email' parameter
    data = {'email': email}

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()  # Check for HTTP errors

        # Display the body of the response
        print(response.text)

    except requests.exceptions.RequestException as e:
        print("Error:", e)
