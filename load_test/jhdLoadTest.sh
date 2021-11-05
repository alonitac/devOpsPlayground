#!/bin/sh
source ../utils.sh

ZZZ=3

while [ 1 ]; do
  http_request
  echo " myIP"
  sleep $ZZZ
done
