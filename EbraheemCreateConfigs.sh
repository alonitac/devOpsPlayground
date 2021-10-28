function checkFolder {
  if test -d $1;then
    ehco "The Folder already exist"
  else
    mkdir $1
  fi
}
function checkFile {
  if test -f ./config/$1;then
    echo "The file already exist"
  else
    touch config2.json
    cp config2.json config2.json
    mv config2.json config2
    cd ./config/
    mv config22.json config.json
  fi

}
