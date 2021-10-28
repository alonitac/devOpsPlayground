function checkFolder {
  if test -d $1;then
    echo "The Folder already exist"
  else
    mkdir $1
  fi
}
function checkFile {
  if test -f ./config/$1;then
    echo "The file already exist"
  else
    checkFolder config
    touch ./config/config.json
    cat config.json > ./config/config.json
  fi
}
checkFile config.json