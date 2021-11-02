source  ../utils.sh


function fun() {
 numOfTests=1;

SLEEP_TIME=5;
while [ true ]; do
  echo test num:$((numOfTests++));
  http_request
  echo ''
  sleep $SLEEP_TIME

done
}

fun