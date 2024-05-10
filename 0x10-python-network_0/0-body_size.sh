#!/bin/bash
# display the size of the body of the response in bytes to a url given as parameter
curl -s -o /dev/null -w "%{size_download}\n" "$1"
