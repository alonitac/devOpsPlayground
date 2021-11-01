#!/usr/bin/env bash
source ../utils.sh
 sleepTime=4
 while [ 1 ]; do
     http_request
     sleep     $sleepTime
     echo " "
 done
     

