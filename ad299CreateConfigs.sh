
if test -f ./configs/config.json; then
  echo "file exists"
cat ./config.json > ./configs/config.json
else
mkdir configs
cd configs
touch config.json
fi


