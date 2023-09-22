"""
This script fetches the URL 'https://alu-intranet.hbtn.io/status' using the 'requests' package
and displays the body of the response with tabulation.
"""

import requests

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)

    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text.replace('\n', '\n\t\t\t')))
