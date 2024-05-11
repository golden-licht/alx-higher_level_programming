#!/usr/bin/python3

""""Handle errors"""

import requests
from sys import argv

if __name__ == '__main__':
    response = requests.get(argv[1])
    status_code = response.status_code
    if (status_code >= 400):
        print('Error code: ', status_code)
    else:
        print(response.text)
