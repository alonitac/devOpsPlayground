#source ./config.json
FILE="./config.json"
if test -f "$FILE"; then
    echo "$FILE exists."
else
  mkdir ./configs/config.json

fi

FILE="./configs/config.json"
if test -f "$FILE"; then
    echo "$FILE exists."
else
  cp config.json configs/config.json

fi
