#!/usr/bin/env bash
source ../utils.sh

SLEEP_TIME=3

while [ 1 ]; do
    http_request
    echo ""
    sleep $SLEEP_TIME
done
