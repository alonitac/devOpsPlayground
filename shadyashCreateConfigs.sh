
if [ -d ./configs ]; then
    echo "configs already exist"
else
    mkdir ./configs
fi

if [ -f ./configs/config.json ]; then
    echo "config.json already exist"
else
    touch ./configs/config.json
fi

cat ./config.json > ./configs/config.json



