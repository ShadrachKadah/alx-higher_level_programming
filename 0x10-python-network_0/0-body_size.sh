#!/bin/bash
# sends a request to the URL at $1 and displays the size of the body of the responese
curl -s "$1" | wc -c
