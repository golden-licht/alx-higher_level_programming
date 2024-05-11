#!/usr/bin/python3

"""Send a request a URL and display the value of the
X-Request-Id variable found in the header of the response."""

import urllib.request
from sys import argv

req = urllib.request.Request(argv[1])
with urllib.request.urlopen(req) as response:
    header = response.info()

print(header.get('X-Request-Id'))
