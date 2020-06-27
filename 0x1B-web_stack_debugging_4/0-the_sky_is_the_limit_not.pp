# values
exec {'Changing value':
path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
command => "sed -i 's/15/5000/g' /etc/default/nginx; sudo service nginx restart",
}
