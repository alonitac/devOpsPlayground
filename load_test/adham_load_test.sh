source ../utils.sh

SLEEP_TIME = 1
while true; do
  http_request
  sleep $SLEEP_TIME
  echo
  done
