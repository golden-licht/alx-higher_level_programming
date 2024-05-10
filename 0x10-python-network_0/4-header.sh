#!/bin/bash
# send a get request together with a header variable
curl -s -H "X-School-User-Id: 98" "$1"
