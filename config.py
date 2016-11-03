# Author: Alex Ksikes

# This is a sample config file. Complete it and rename the file config.py.

import web, os

from app.helpers import misc
from app.helpers import utils

# connect to database
db = web.database(dbn='mysql', db='mlss', user='<mysql_user>', passwd='<mysql_password>')

# in development debug error messages and reloader
web.config.debug = True

# in develpment template caching is set to false
cache = False

# global used template functions
globals = utils.get_all_functions(misc)

# the domain where to get the forms from
site_domain = '<domain.com>'

# set global base template
view = web.template.render('app/views', cache=cache,  globals=globals)

# used as a salt
encryption_key = '<a random string>'

# important dates
date_application_deadline = '<May 30th, for example>'
date_amission_notification = '<June 15th>'
date_referee_deadline = '<June 5th>'

# email settings
mail_sender = '<email that sends every message>'
mail_reply_to = '<email that will receive replies>'
webmaster = '<email that receives the bugs>'

# in production the internal errors are emailed to us
web.config.email_errors = webmaster

## here I use the gmail smtp server
web.config.smtp_server = 'smtp.gmail.com'
web.config.smtp_port = 587
web.config.smtp_username = mail_sender
web.config.smtp_password = '<your password for mail_sender>'
web.config.smtp_starttls = True
