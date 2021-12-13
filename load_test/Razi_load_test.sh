
SLEEP_TIME=1

function http_request {
  curl http://www.ifconfig.me
}

while [ 1 ] ;do
 http_request
 sleep $SLEEP_TIME
echo " "

done



