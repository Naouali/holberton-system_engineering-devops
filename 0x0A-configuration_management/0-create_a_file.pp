resource_type { '/tmp/Holberton':
	path => /tmp/holberton,
	ensure => file,
	content => "I Love Puppet",
	group => www-data,
	owner => www-data,
	mode => 0744,
}
