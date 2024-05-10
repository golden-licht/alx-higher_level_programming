#!/bin/bash
# send a delete request, instead of the default GET request
curl -sX DELETE "$1"
