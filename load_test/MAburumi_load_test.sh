#1/bin/bash
source ../utils.sh
SLEEP_TIME=1

while [ $SLEEP_TIME -gt 0 ];do
{
  echo "Ip :  "
  http_request
  echo " "
  sleep $SLEEP_TIME
}
done

