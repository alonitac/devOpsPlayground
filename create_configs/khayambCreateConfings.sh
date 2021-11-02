#!/bin/sh
function configJasonUpdate {

  if  test ! -d ./configs ;then

    mkdir configs

  fi

  if test -f ./configs/config.json ;then

    echo "config.json is going to be overwritten"

  fi

  cat ./config.json > ./configs/config.json

}

configJasonUpdate






