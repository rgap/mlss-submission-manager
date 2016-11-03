# Author: Alex Ksikes

# TODO:
# - this should be moved to a DB.

import web
import config

mail_headers = {'Reply-To': config.mail_reply_to}

msg_to_applicant = \
'''$def with (applicant, body)
Dear $applicant.first_name $applicant.last_name,

$body

Best wishes,
The Organizers.
--------------------------------------------------------------
Machine Learning Summer School 2016 Arequipa, Peru
Organizing Team
www.ucsp.edu.pe/ciet/mlss16
--------------------------------------------------------------
'''

def to_applicant(applicant, subject, body):
    msg = web.template.Template(msg_to_applicant)(applicant, body)
    web.sendmail(config.mail_sender, applicant.email, subject, msg, headers = mail_headers)
