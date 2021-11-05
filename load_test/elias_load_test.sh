#!/bin/bash
source ./utils.sh

function http_request {
  curl http://www.ifconfig.me
}

while true ; do #tests ifconfig.com every 3 secs
  http_request
  echo " overflow test will run every 3 sec's "

  sleep 3 $SLEEP_TIME
   echo "by (elias)"

done