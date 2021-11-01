
function configJasonUpdate {

  if  [ ! -d ./configs ];then

    mkdir configs

  fi

  if [ -f ./configs/config.json ];then

    echo "config.json is going to be overwritten"

  fi

  cat ./config.json > ./configs/config.json

}

configJasonUpdate






