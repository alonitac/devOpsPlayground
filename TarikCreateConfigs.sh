




function  fileContentCopy {

 if [ -d  configs ] ;then
 if [ -f  configs/config.json  ] ;then
echo 'directory and file already exist . '

else
  touch configs/config.json

fi

else
mkdir configs
touch configs/config.json


fi


cat config.json > configs/config.json

}


fileContentCopy



