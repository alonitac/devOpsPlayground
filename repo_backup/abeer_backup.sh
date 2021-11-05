#!/bin/bash
source ../utils.sh
file="repo_backup.tar.gz"
function filesBackup() {
  if [  -f $file ]; then
    echo "File exist, it will be overwritten, here is the file details"; stat $file
  fi
  tar -czvf $file ../
  echo "Total files: ";total_files ../
  echo "Total directories: ";total_directories ../
  echo "The date is"; date
  echo "User name: "; whoami
}
filesBackup



