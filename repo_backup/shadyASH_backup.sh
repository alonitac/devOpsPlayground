source ../utils.sh
#check if given path for the backups directory exist
if [ -d "$1" ]; then
  #the path does exist continue
  echo "path is Valid continue."
  #if the repo_backup.tar.gz exist we warn the user that we are gonna overwrite it otherwise we tell the user that we created a backup file
  if [ -f "$1"/repo_backup.tar.gz ]; then
    echo "repo_backup is gonna be overwritten"
  else
    echo "backup file have been created"
  fi
  #tar -cf (path where you gonna put the tar file) (path for the directory you want to compress to a tar)
  tar -cf "$1"/repo_backup.tar.gz ./
  #print Details of the backup
  NUMBERFILES= find -type f | wc -l
  NUMBERDIRECTORIES= find -type d | wc -l
  USER=$(whoami)
  echo "$NUMBERFILES  $NUMBERDIRECTORIES $USER"
else
  echo "path is not Valid Operation Stopt!"
fi