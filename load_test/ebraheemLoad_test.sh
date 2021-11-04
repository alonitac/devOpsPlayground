source ../utils.sh
SLEEP_TIME=3
sleep 1
http_request
echo ""
COUNTER=1
while [ $COUNTER -lt 3 ];do
  http_request
  echo ""
  sleep ${SLEEP_TIME}
  COUNTER=$((COUNTER+1))
done
