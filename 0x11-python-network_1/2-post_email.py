#!/usr/bin/python3

"""Send a POST request to passed URL with email as parameter"""

import urllib.parse
import urllib.request
from sys import argv

if __name__ == '__main__':
    url, email = argv[1:]
    values = {'email': email}
    data = urllib.parse.urlencode(values)  # to string
    data = data.encode('utf-8')  # to bytes
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        body = response.read()

    print(body.decode('utf-8'))
