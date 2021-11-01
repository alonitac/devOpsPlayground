source ./utils.sh

#!/bin/bash #the first line of the bash script
BACKUPTIME=`date +%b-%d-%y` #current date

./home/usr/path/backup-$BACKUPTIME.tar.gz #create a backup file using the current date in it's name of the backup file

./home/usr/path/elias_repos  #the folder that contains the files that we want to backup

function compress {
tar -cpzf /home/usr/path/backupdir $../home/usr/path/ #create the backup

echo "Backup Files  $(total_files ${url})"

echo "By $(whoami) at $(date)"

}

