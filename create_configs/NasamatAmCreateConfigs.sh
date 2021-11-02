if [test !-d ./configs ]; then
  mkdir configs
else
  echo "The directory is already exist!"
fi

if [test !-f ./configs/config.json]; then
  touch configs/config.json
else
  echo "The file is already exist!"
fi

 cat  config.json > ./configs/config.json