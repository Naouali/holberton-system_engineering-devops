#resource to kill a process
package {'pkill':
ensure => 'installed',
}
exec {'kill':
command =>'/usr/bin/pkill -f ./killmenow',
}
