cnf_path=" ./configs/config.json"
if [ ! -d ./configs ] ; then

mkdir ./configs
fi

touch configs/config.json



if [ -f configs/config.json ];
then
  echo "file already exists"
  fi

cat config.json > $cnf_path


