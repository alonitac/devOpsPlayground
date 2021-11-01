function http_request {
  curl http://www.ifconfig.me
}
while true; do
   http_request
   echo " "
   sleep 2
   done
