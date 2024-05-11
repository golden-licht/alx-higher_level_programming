#!/usr/bin/python3

"""Send a POST request to the passed URL with email as a parameter"""

import requests
from sys import argv

if __name__ == '__main__':
    url, email = argv[1:]
    response = requests.post(url, data={'email': email})
    print(response.text)
