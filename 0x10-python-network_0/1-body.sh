#!/bin/bash
#X: define cúal opción(GET, POST...) L: location
curl -s -X GET "$1" -L 200
