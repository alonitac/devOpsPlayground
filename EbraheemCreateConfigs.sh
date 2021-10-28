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
    touch config2.json
    cp config.json config2.json
    mv config2.json config
    cd ./config/
    mv config2.json config.json
  fi

}
checkFolder config
checkFile config.json