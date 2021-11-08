source ./utils.sh
if test -d $1; then
  echo "The path exists"
  if test -f $1/repo_backup.tar.gz;then
    echo "Warning:The file repo_backup.tar.gz is already exists and it will be overwritten"
    stat $1/repo_backup.tar.gz
  fi
    tar -czf $1/repo_backup.tar.gz .
    echo "Total files is: "
    total_files $1/repo_backup.tar.gz
    echo "Total directories is: "
    total_directories $1/repo_backup.tar.gz
    echo "The date is: "
    date
    echo "Whoami is: "
    whoami
else
  echo "This path doesnt exist"

fi
