source ../utils.sh

if [ -d $HOME ]; then
  echo "the path exists"
  if [ -f $HOME/adbackup.tar ]; then
    echo "warning:this file is already exists and it will be overwritten"
    tar -cvf $HOME/adbackup.tar ./
    total_files
    total_directories
    date
    whoami
  fi
else
  echo "this path doesnt exist"
fi
