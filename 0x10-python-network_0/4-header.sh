#!/bin/bash
#sends a GET request to the URL, and displays the body of the response, H: header
curl -sX GET "$1" -H "X-HolbertonSchool-User-Id: 98"
