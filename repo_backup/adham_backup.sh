source ../utils.sh
#checking if the path for saving the backup file is exist
if [ -d .. ]; then
  echo "the path is exist"
  #checking if the backup file is already exist
  if [ -f ../repo_backup.tar.gz ]; then
    echo "warning:this file is already exist and it will be overwritten"
    echo "this file contains the following details:"
    echo
    echo $(stat ../repo_backup.tar.gz)
    fi
    tar -czvf ../repo_backup.tar.gz ../
    echo "total files: $(total_files ../)"
    echo "total directories: $(total_directories ../)"
    echo "date: $(date)"
    echo "user: $(whoami)"
  #checking if the path is not exist
else
  echo "this path is not exist"
fi
