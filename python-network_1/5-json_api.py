"""
This script takes a letter as input and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter (q). It processes the response and displays the result.

Usage: python script.py <letter>

If no letter argument is given, it sets q="" by default.

If the response body is properly JSON formatted and not empty, it displays the id and name like this:
[<id>] <name>

Otherwise:
- Displays "Not a valid JSON" if the JSON is invalid.
- Displays "No result" if the JSON is empty.

You must have the 'requests' and 'sys' packages installed.

Example: python script.py A
"""

import requests
import sys

if __name__ == "__main__":
    # Check if a letter is provided as a command-line argument
    if len(sys.argv) != 2:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': q}

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()  # Check for HTTP errors

        # Try to parse the JSON response
        try:
            user_info = response.json()
            if isinstance(user_info, dict) and 'id' in user_info and 'name' in user_info:
                print("[{}] {}".format(user_info['id'], user_info['name']))
            else:
                print("No result")

        except ValueError:
            print("Not a valid JSON")

    except requests.exceptions.RequestException as e:
        print("Error:", e)
