source utils.sh
url="$(pwd)"
function compress {
  tar -czvf ${1}.tar.gz ${url}
  echo "Backup Files  $(total_files ${url})"
  echo "Backup Dic $(total_directories ${url})"
  echo "By $(whoami) in Date $(date)"
}
compress ebraheem

