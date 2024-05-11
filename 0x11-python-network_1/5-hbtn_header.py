#!/usr/bin/python3

"""Send a request a URL and display the value of the
X-Request-Id variable found in the header of the response."""

import requests
from sys import argv

if __name__ == '__main__':
    response = requests.get(argv[1])
    header = response.headers
    print(header.get('X-Request-Id'))
