#mkdir configs
#touch ./configs/config.json
   # cp config.json ./configs/config.json

if [ -d ./configs ]; then
  echo "dir already exist"
  else
     mkdir configs
    fi

    if [ -f ./configs/config.json ]; then
  echo "file already exist"
  else
     touch ./configs/config.json
    cp config.json ./configs/config.json
    fi



