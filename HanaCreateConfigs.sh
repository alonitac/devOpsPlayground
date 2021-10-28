if [ test -d ./configs ]; then
  mkdir configs
else
  echo "The directory is already exist!"
fi


if [test ! -f ./configs/config.json]; then
  touch ./configs/config.json
  cat./config.json >./configs/configs.json
else
  echo "configs.json is already exist in the directory!"
fi
