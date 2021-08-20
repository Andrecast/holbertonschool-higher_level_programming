#!/bin/bash
#script that sends a request to a URL passed as an argument, and displays only the status code of the response
curl -s -I -o -L -w "%{http_code}" "$1"
