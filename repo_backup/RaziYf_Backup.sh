source ../utils.sh
function CompressBackUpRepos
{
 tar -CZF repo_backup.tar.gz ./devOpsPlayground
  stat  [-f repo_backup.tar.gz ]
  echo " there is a BackUp files and backup directory"
   echo " the files are "
    $(total files)
  echo " dir are : "
    $(total directories)
  echo "this has been made by : $(whoami)"
  echo "The date is  : $(date)"

}
  if tar -XF repo_backup.tar.gz -C ./devOpsPlayground
    [ Test -d 'repo_backup.tar.gz']; then
     echo " RepoBackUp exist"
   else
     mkdir repo_backup
      echo "Dir BackUP Created"
  fi


