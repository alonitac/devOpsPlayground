#!/bin/bash
# In windows OS use: #!/bin/sh

source ../utils.sh

SLEEP_TIME=0.1

# Also a valid code:
# while [ 1 ]; do
# while [ true ]; do
while true; do
  http_request
  echo "done"
  sleep $SLEEP_TIME
done
