ssh-authorized_keys {'ubuntu@35.185.93.202'
ensure => 'present',
user =>'ubuntu',
type => 'ssh-rsa',
key => '~/.ssh/holberton',
}
