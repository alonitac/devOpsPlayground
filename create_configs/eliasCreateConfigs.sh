#!/bin/sh

if [ ! -d ./configs ]; then
  mkdir  configs
else
   echo "directory exists"
fi


if [ -f ./configs/config.json ]; then
  echo "file exist"
fi

cat ./config.json > ./configs/config.json