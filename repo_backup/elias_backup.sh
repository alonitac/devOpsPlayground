source ./utils.sh
# commands used: 1 adding devopsPlayground to ubuntu by using command : git clone https://github.com/alonitac/devOpsPlayground
#2 : compressing by: tar -czvf repo_backup.tar.gz ~/git_workspace/devOpsPlayground
#!/bin/bash #the first line of the bash script

#git clone  https://github.com/alonitac/devOpsPlayground #for does who don't have the repo inside their ubuntu

function compress {
tar -czvf repo_backup.tar.gz ~/DevOpsplayGound

echo "Back up Files  $(total_files ${url})"
echo "Backup Dic $(total_directories ${url})"

  echo "By $(whoami) in Date $(date)"
}
 if [ -f "$1"/repo_backup.tar.gz ]; then
    echo "single.tar.gz is gonna be overwritten"
  else
    echo "backup file have been created"
  fi

