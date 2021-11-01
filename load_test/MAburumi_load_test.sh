#1/bin/bash
source ../utils.sh
SLEEP_TIME=0.2

while [ 1 ];do
{
  echo "Ip :  "
  http_request
  echo " "
  sleep $SLEEP_TIME
}
done

