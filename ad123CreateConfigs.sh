
if test ! -d ./configs; then
   mkdir  configs
else
   echo "directory exists"
fi

if test -f ./configs/config.json; then
  echo "warning: this file is already exists"
else
   touch  ./configs/config.json
   cat ./config.json >./configs/config.json
fi



