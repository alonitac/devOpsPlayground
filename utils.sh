# The function total_files reports a total number of files for a given directory.
function total_files {
  find $1 -type f | wc -l
}

# The function total_directories reports a total number of directories
# for a given directory.
function total_directories {
  find $1 -type d | wc -l
}
function http_request
{
  curl http://www.ifconfig.me
}



