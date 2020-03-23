file { '/tmp/Holberton':
	path => '/tmp/holberton',
	ensure => 'present',
	content => 'I Love Puppet',
	group => 'www-data',
	owner => 'www-data',
	mode => '0744',
}
