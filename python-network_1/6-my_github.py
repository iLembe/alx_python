"""
This Python script takes your GitHub credentials (username and personal access token) as arguments and uses Basic Authentication
with the GitHub API to display your GitHub user ID. Only the 'read:user' permission is needed for this operation.

Usage: python script.py <username> <personal_access_token>

Arguments:
    <username>: Your GitHub username.
    <personal_access_token>: Your personal access token for authentication.

You must have the 'requests' and 'sys' packages installed.

Example:
    python script.py your_username your_personal_access_token

Note: Make sure to keep your personal access token secure and do not share it with others.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <username> <personal_access_token>")
        sys.exit(1)

    username = sys.argv[1]
    personal_access_token = sys.argv[2]

    # Create a Basic Authentication header with your personal access token as the password
    auth = (username, personal_access_token)

    # Make a GET request to the GitHub API to fetch your user information
    url = "https://api.github.com/user"
    try:
        response = requests.get(url, auth=auth)

        if response.status_code == 200:
            user_info = response.json()
            user_id = user_info.get("id")
            if user_id is not None:
                print("Your GitHub user ID is:", user_id)
            else:
                print("Failed to fetch user ID.")
        else:
            print("Failed to authenticate with GitHub. Status code:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("Error:", e)
