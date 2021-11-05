source ./utils.sh

if test -d $1;then
    echo "The path exists"
  if test -f $1/repo_backup.tar.gz; then
    echo "The file is already exists and it will overwritten"
    stat $1/repo_backup.tar.gz
  fi
  tar -czf $1/repo_backup.tar.gz .
  echo "The number of files were backed up:"
  total_files $1/repo_backup.tar.gz
  echo "The number of directories were backed up:"
  total_directories $1/repo_backup.tar.gz
  echo "The date is:"
  date
  echo "The Linux user that ran the script:"
  whoami

else
  echo "The path exists"
fi
