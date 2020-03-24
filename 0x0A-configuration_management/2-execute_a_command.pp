#resource to kill a process
package {'pkill':
ensure => 'installed',
}
exec {'killmenow':
command =>'pkill',
}
