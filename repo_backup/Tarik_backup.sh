# Note : given path should end with directory name, otherwise unexpected results such as(/ , ../ ).

source  ../utils.sh # import/include helper functions .

function backupRepos {


  if  [ ! -d  $1 ] || [ $# -le 0 ] ; then #check if the path is valid or if a path was given.
      echo 'no such path';
      return
  fi

  if [  -f $1/repo_backup.tar.gz ]; then   # check if file is exist
    echo 'WARNING : FILE WILL BE OVERWRITTEN!'
    echo 'File Info --------------------------------------------------------'
    stat $1/repo_backup.tar.gz  #show some info about this file.
    echo '--------------------------------------------------------'
  fi

# create archive and compress repos files, --overwrite used to overwrite file if exist.
  tar  -cf  $1/repo_backup.tar.gz ../../devOpsPlayground --overwrite
  # -e  option used to allow escape char interpretation in a string .
  # Note : "" was used instead of '' to evaluate variables in the string.
  echo 'Repos Info--------------------------------------------------------'
  echo -e "total files:$(total_files)\ntotal dirictories:$(total_directories)\ndate:$(date)\ncurrent user:$(whoami)"
  echo '--------------------------------------------------------'

}
backupRepos $1 # global scope $1 refer to global arg.



