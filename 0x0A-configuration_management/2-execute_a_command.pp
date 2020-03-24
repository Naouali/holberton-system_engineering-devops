#resource to kill a process
exec {'kill':
command =>'/usr/bin/pkill -f ./killmenow',
}
