#!/bin/sh

source ../utils.sh

function compressedBackup {

BU_DIR="../../backUpTest"

  if [ -d $BU_DIR ] ;  then

    if [ ! -f ./repo_backup.tar.gz ] ; then

        tar -zxf ./repo_backup.tar.gz -C $BU_DIR
       echo   $total_files "./repo_backup.tar.gz"
       date
       echo USER=$(whoami)

    else

        stat ./repo_backup.tar.gz
        echo " Existing Backup File OverWritten"
        tar -zxf ./repo_backup.tar.gz -C $BU_DIR
        echo   $total_files "./repo_backup.tar.gz"
        date
        echo  USER=$(whoami)
    fi
  else

     echo "No Such Dir - Backup Failed"

  fi

}



compressedBackup


