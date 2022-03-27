check_ping(){
   for PID in $(pgrep -f "${EXE_NAME}"); do
       echo $PID
       lsof -t $(which "$EXE_NAME")
   done
}

check_ping

