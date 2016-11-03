# MLSS Submission Manager

This is an application based on https://github.com/alexksikes/MLSS

I corrected some bugs and added more functionalities and it was used to process a vast number of applicants for the machine learning summer shcool (MLSS) 2016 located in Peru. 

## Installation

Some steps may be missing, if something is missing let me know about it.

1) Install webpy, I certainly know it is a pretty old framework. After having tried installing it in MacOS, I couln't, so I think it will only work in a Linux distribution, like Ubuntu.

Follow these instructions: http://webpy.org/install

2) Setup the database: mysql -p mlss < ./schema.sql. Note you first need to create a database called mlss.

3) Check out "application.py". It contains some important global variables that used in the entire application.

```
# connect to database
db = web.database(dbn='mysql', db='mlss', user='<mysql_user>', passwd='<mysql_password>')
...
# the domain where to get the forms from
site_domain = '<domain.com>'
...
# used as a salt
encryption_key = '<a random string>'
...
# important dates
date_application_deadline = '<May 30th, for example>'
date_amission_notification = '<June 15th>'
date_referee_deadline = '<June 5th>'
...
# email settings
mail_sender = '<email that sends every message>'
mail_reply_to = '<email that will receive replies>'
webmaster = '<email that receives the bugs>'
...
web.config.smtp_password = '<your password for mail_sender>'
```

4) Now you can run it

python ./application.py

## On a remote server

1) Setup lighttpd

In my case, I cloned the repository in /var/www/MLSS, in an Ubuntu VPS. Therefore, my /etc/lighttpd/lighttpd.conf file looked like this

```
server.modules = (
        "mod_access",
        "mod_alias",
        "mod_compress",
        "mod_redirect",
        "mod_rewrite",
        "mod_fastcgi",
        "mod_accesslog",
)

name = "root"

server.document-root        = "/var/www"
server.upload-dirs          = ( "/var/cache/lighttpd/uploads" )
server.errorlog             = "/var/log/lighttpd/error.log"
server.pid-file             = "/var/run/lighttpd.pid"
server.username             = "www-data"
server.groupname            = "www-data"
server.port                 = 800

###

# make sure users can access the application forms but not the admin
    $HTTP["url"] !~ "/(submit_admitted|submit_application|submit_reference|css|$
        auth.require = ( "" =>
        (
           "method" => "digest",
           "realm" => "Authorized users only",
           "require" => "valid-user",
        ))
    }

#############

index-file.names            = ( "index.php", "index.html", "index.lighttpd.html$
url.access-deny             = ( "~", ".inc" )
static-file.exclude-extensions = ( ".php", ".pl", ".fcgi" )

compress.cache-dir          = "/var/cache/lighttpd/compress/"
compress.filetype           = ( "application/javascript", "text/css", "text/htm$

# default listening port for IPv6 falls back to the IPv4 port
include_shell "/usr/share/lighttpd/use-ipv6.pl " + server.port
include_shell "/usr/share/lighttpd/create-mime.assign.pl"
include_shell "/usr/share/lighttpd/include-conf-enabled.pl"
```

And my /etc/lighttpd/conf-available/10-fastcgi.conf

```
# /usr/share/doc/lighttpd/fastcgi.txt.gz
# http://redmine.lighttpd.net/projects/lighttpd/wiki/Docs:ConfigurationOptions#$

server.modules += ( "mod_fastcgi" )
server.modules += ( "mod_rewrite" )

script = "/var/www/MLSS/application.py"

url.rewrite += (
        # Commented for development
        #"^/img/(.*)$" => "/img/$1",
        #"^/css/(.*)$" => "/css/$1",
        #"^/js/(.*)$" => "/js/$1",

        "^/resumes/(.*)$" => "/resumes/$1",
        "^/(.*)$" => script + "/$1",
    )

    fastcgi.server += ( script =>
    ((
        "socket" => "/tmp/" + name + var.PID + ".socket",
        "bin-path" => script,
        "check-local" => "disable",
        "max-procs" => 1,
        "bin-environment" => (
            "REAL_SCRIPT_NAME" => ""
        ),
    ))
    )
```

2) Make sure lighttpd has write access to the directory ./public/resumes/
You'd do something like this: sudo chgrp www-data ./public/resumes; chmod 775 ./public/resumes;

3) Restart lighttpd

sudo /etc/init.d/lighttpd restart

4) Run it

python ./application.py <IP address>:80

I recommend you use "screen" to run in on background.
And you can remove the folder "static_demo" because it's just the static demo of the application.

## Online demo

http://htmlpreview.github.io/?https://github.com/rgap/mlss-submission-manager/static_demo/index.html

## Suggestions

For questions / suggestion email me, Rel Guzman (r.guzmanap at gmail dot com). Or submit an issue.

## License

GNU GPL
