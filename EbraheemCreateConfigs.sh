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
//method 2
function checkfile2 {
  if test -f ./config/$1;then
    echo "The file already exist"
  else
    checkFolder config
    touch config2.json
    cp config.json config2.json
    mv config2.json config
    mv config2.json config.json
  fi
}

checkFile config.json