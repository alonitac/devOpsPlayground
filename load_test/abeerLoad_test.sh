#!/bin/bash
source ../utils.sh
SLEEP_TIME=2;
sleep 1
http_request
while true; do
  http_request
  sleep $SLEEP_TIME
done