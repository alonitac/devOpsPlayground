source ./config.json
mkdir ./configs/config.json
cp config.json configs/config.json

# shellcheck disable=SC1073
function fileExsits {
# shellcheck disable=SC1073
if test configs -d; then
  echo "ok"
else
  mkdir configs
fi


if test configs/config.json -f; then
  echo "already exists"
else
  touch configs/config.json
fi

}

