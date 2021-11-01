#!/bin/bash

source ../utils.sh

SLEEP_TIME=3
while [ true ]; do
  http_request
  echo "ok"
  sleep $SLEEP_TIME
done
