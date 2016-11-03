# -*- coding: utf-8 -*-
# Author: Alex Ksikes

# TODO:
# - this should be moved to a DB.

import web
import config

## EDITED BY: rgap
## mail copies are actually unnecesary
#bcc = 'admin@mlss-arequipa-applications.com'

msg_to_applicant = \
'''$def with (applicant)
Dear $applicant.first_name $applicant.last_name,

Your application for the Machine Learning Summer School in Arequipa, Peru has been received. We will contact $applicant.referee_name  and ask for a letter of reference. Both you and the referee will receive notification once the letter has been received. Decisions on applications will be emailed on %s.

Thank you very much for applying.

And please if you have any question, don't ask it to the admin email, reply to this message or send a message to one of the organizers http://www.ucsp.edu.pe/ciet/mlss16/organizers.html

Best wishes,
The Organizers.
--------------------------------------------------------------
Machine Learning Summer School 2016 Arequipa, Peru
Organizing Team
www.ucsp.edu.pe/ciet/mlss16
--------------------------------------------------------------
''' % config.date_amission_notification

msg_to_applicant_simple = \
'''$def with (applicant)
Dear $applicant.first_name $applicant.last_name,

Your application for the Machine Learning Summer School in Arequipa, Peru has been received. Decisions on applications will be emailed on %s.

Thank you very much for applying.

And please if you have any question, don't ask it to the admin email, reply to this message or send a message to one of the organizers http://www.ucsp.edu.pe/ciet/mlss16/organizers.html

Best wishes,
The Organizers.
--------------------------------------------------------------
Machine Learning Summer School 2016 Arequipa, Peru
Organizing Team
www.ucsp.edu.pe/ciet/mlss16
--------------------------------------------------------------
''' % config.date_amission_notification

msg_to_referee = \
'''$def with (applicant)
Dear $applicant.referee_name,

$applicant.first_name $applicant.last_name has applied for the Machine Learning Summer School 2016 in Arequipa, Peru and named you as referee.

We expect to receive more applications for the summer school than there are places available, and will select participants based on their academic background. We would ask you to submit a letter of reference that helps us evaluate the applicant's qualification. Your letter should address the applicant's background and potential in Machine Learning, academic standing compared to other students, and how the student would benefit from attending MLSS 2016. If the applicant wishes to apply for financial support (we will be able to provide support to a limited number of participants), please include a paragraph explaining why such support is required. Otherwise, we will not consider the applicant for financial support.

Your letter can be entered as plain text under the following URL:

http://%s/submit_reference/$applicant.secret_md5

For more information about the summer school, please refer to

http://www.ucsp.edu.pe/ciet/mlss16/

Thank you very much.

And please if you have any question, don't ask it to the admin email, reply to this message or send a message to one of the organizers http://www.ucsp.edu.pe/ciet/mlss16/organizers.html

Best wishes,
The Organizers.
--------------------------------------------------------------
Machine Learning Summer School 2016 Arequipa, Peru
Organizing Team
www.ucsp.edu.pe/ciet/mlss16
--------------------------------------------------------------
''' % config.site_domain

msg_notify_applicant = \
'''$def with (applicant)
Dear $applicant.first_name $applicant.last_name,

This is to inform you that your letter of reference for the Machine Learning Summer School 2016 has been received. You should receive a decision on your application on %s.

And please if you have any question, don't ask it to the admin email, reply to this message or send a message to one of the organizers http://www.ucsp.edu.pe/ciet/mlss16/organizers.html

Best wishes,
The Organizers.
--------------------------------------------------------------
Machine Learning Summer School 2016 Arequipa, Peru
Organizing Team
www.ucsp.edu.pe/ciet/mlss16
--------------------------------------------------------------
'''% config.date_amission_notification

msg_notify_referee = \
'''$def with (applicant)
Dear $applicant.referee_name

Your letter of reference for $applicant.first_name, $applicant.last_name has been received.
Thank you very much for your assistance.

And please if you have any question, don't ask it to the admin email, reply to this message or send a message to one of the organizers http://www.ucsp.edu.pe/ciet/mlss16/organizers.html

Best wishes,
The Organizers.
--------------------------------------------------------------
Machine Learning Summer School 2016 Arequipa, Peru
Organizing Team
www.ucsp.edu.pe/ciet/mlss16
--------------------------------------------------------------
'''

msg_resend_password = \
'''$def with (user)
Hello $user.nickname, 

Here are the login information you have requested:

login: $user.email
password: $user.password

And please if you have any question, don't ask it to the admin email, reply to this message or send a message to one of the organizers http://www.ucsp.edu.pe/ciet/mlss16/organizers.html

Best wishes,
The Organizers.
--------------------------------------------------------------
Machine Learning Summer School 2016 Arequipa, Peru
Organizing Team
www.ucsp.edu.pe/ciet/mlss16
--------------------------------------------------------------
'''

first_msg_to_admitted_applicant = \
'''$def with (applicant)
Dear $applicant.first_name $applicant.last_name,

We are very happy to inform you that your application to the Machine Learning Summer School'16 in Peru has been accepted.

We have received a record 210 applications for this summer school, yet could only accept about 120 candidates.

================ Registration Fee ================

To preserve your vacancy, you must pay 400 USD between June 21 and July 8. You will receive a link to make the payment in a few days.

This includes:

- Access to all sessions
- Coffee-breaks
- USB of the tutorials
- Souvenir shirt

=========== Request for Financial Support ===========

We regret to inform you that we are not able to provide you with financial support to support your participation to the MLSS.

The selection process was extremely competitive as we have received many requests from outstanding students from around the world, many of whom are either too young to receive lab funding or whose institution cannot support their travel in any way. We have considered every possible aspect to reach this decision, and have closely examined your request (as well as a mention, or not, of that request in your recommender's letter).

We are sorry for this disappointing outcome. We do sincerely hope, however, that you have managed to secure enough funds on your side to join us this summer.

================ Additional Notes ================

Please if you have any question, don't ask it to the admin email, reply to this message or send a message to one of the organizers http://www.ucsp.edu.pe/ciet/mlss16/organizers.html

Best wishes,
The Organizers.
--------------------------------------------------------------
Machine Learning Summer School 2016 Arequipa, Peru
Organizing Team
www.ucsp.edu.pe/ciet/mlss16
--------------------------------------------------------------
'''

pay_msg_to_admitted_applicant = \
'''$def with (applicant)
Dear $applicant.first_name $applicant.last_name, as you already know, your application to the Machine Learning Summer School'16 in Peru has been accepted.

Now, we need your Passport number or DNI if you are Peruvian, also check if your full name is correct for your certificate.

Enter to the following URL to continue with the payment, where also you can find additional information.

http://%s/submit_admitted/$applicant.secret_md5


================ Registration Fee ================

We also remind you that your registration fee will only cover:

- Access to all sessions
- Coffee-breaks
- USB of the tutorials
- Souvenir shirt


=================== Visa =====================

Most of the citizens from countries around the world are not required to apply for a visa to enter to Peru (for stages up to 90 days), you may not even need a Visa to come to the summer school. Please check out the following page in order to know if you need one:

http://www.limaeasy.com/images/documents/visa/visa-peru-countries.pdf

If this is required for you, then you will probably need some visa assistance, please send an e-mail to Ximena Aranzaens (mazuniga@ucsp.edu.pe), and she will contact you.

For more information: http://www.ucsp.edu.pe/ciet/mlss16/travel.html


================ Additional Notes ================

Please if you have any question, don't ask it to the admin email, reply to this message or send a message to one of the organizers http://www.ucsp.edu.pe/ciet/mlss16/organizers.html


Best wishes,
The Organizers.
--------------------------------------------------------------
Machine Learning Summer School 2016 Arequipa, Peru
Organizing Team
www.ucsp.edu.pe/ciet/mlss16
--------------------------------------------------------------
''' % config.site_domain


msg_to_rejected_applicant = \
'''$def with (applicant)
Dear $applicant.first_name $applicant.last_name,

Thank you very much for submitting your application to the Machine Learning Summer School. We received an unprecedented 210 applications. Since the number of available places is limited by the size of our venue to 120 participants.

Unfortunately, your application was among those which were not successful. We will not be able to offer you a place in the Machine Learning Summer School this year.

We are very sorry to have to disappoint you in this way. Because the high level of competition for places forced us to reject many applicants. Many of them are highly qualified and eager to participate - people who we are convinced would have contributed greatly to the school. But there is simply not enough space in our building to seat them all.

================ Additional Notes ================

And please if you have any question, don't ask it to the admin email, reply to this message or send a message to one of the organizers http://www.ucsp.edu.pe/ciet/mlss16/organizers.html

Best wishes,
The Organizers.
--------------------------------------------------------------
Machine Learning Summer School 2016 Arequipa, Peru
Organizing Team
www.ucsp.edu.pe/ciet/mlss16
--------------------------------------------------------------
'''


first_msg_to_attendee = \
'''$def with (applicant)
Dear $applicant.first_name $applicant.last_name,

Thank you very much for applying to the MLSS 2016 in Arequipa, you are all welcome.

I want to send you some information:

1. Poster Sessions

- All poster will be printed here, the cost is $$ 4.00 USD (approximately 12.00 peruvian soles)
- The size of the poster is 79.5x 60.5 cm, you can use the format A0 when making the poster.
- You must submit your poster in PDF format until 29 July to Jose Ochoa (jeochoa@ucsp.edu.pe).
- The schedule of the poster sessions will be published on 01 August.

2. Practical sessions

- Some speakers plan to conduct practical sessions, please bring your laptops with Matlab (any version) and Python installed. If anyone has difficulty to bring a laptop please send an email to Rel Guzman (r.guzmanap@gmail.com), we will provide a laptop within the university.

3. Social Activities

- With the support of the Pasos Andinos tour operator, we have prepared different activities so that you all can enjoy on 6 and 7 August. The details can see them on the following link http://www.ucsp.edu.pe/ciet/mlss16/trekking.html. Please choose your options until July 31, this is important because we are in peak tourist season and we need to make reservations in advance.
- On Monday, August 2, from 16:45 to 19:00 you will have an open get-together, so we can know better each other.

5. The final schedule and times are already placed on the event website.

6. We have created a Facebook group to share the experience of this Summer School, please those interested in joining us, find us with the name Machine Learning Summer School. You can also send us an invitation.

7. On the webpage, you can find the contact information of the organizing committee, do not hesitate to contact any of us.


Finally, thank you for your visit and hope this will be a fruitful and unforgettable experience for all of you.



--------------------------------------------------------------
Efraín Mayhua
Machine Learning Summer School 2016
Arequipa - Perú
www.ucsp.edu.pe
--------------------------------------------------------------
'''


second_msg_to_attendee = \
'''$def with (applicant)
Dear $applicant.first_name $applicant.last_name,

This email is to let you know that we have updated the website and that we will be sending emails through a different email address, arequipa.mlss@gmail.com, so please check your spam folder and unmark our emails as spam if they end up there.


Hoping to see you soon,
The Organizers.
--------------------------------------------------------------
Machine Learning Summer School 2016 Arequipa, Peru
Organizing Team
www.ucsp.edu.pe/ciet/mlss16
--------------------------------------------------------------
'''


mail_headers = {'Reply-To': config.mail_reply_to}

def to_applicant(applicant):
    subject = 'MLSS 2016: Thank You for Your Application'
    msg = web.template.Template(msg_to_applicant)(applicant)
    web.sendmail(config.mail_sender, applicant.email, subject, msg, headers = mail_headers)

def to_applicant_simple(applicant):
    subject = 'MLSS 2016: Thank You for Your Application'
    msg = web.template.Template(msg_to_applicant_simple)(applicant)
    web.sendmail(config.mail_sender, applicant.email, subject, msg, headers = mail_headers)

def to_referee(applicant):
    subject = 'Request for Reference Letter for MLSS 2016 - Deadline: ' + config.date_referee_deadline
    msg = web.template.Template(msg_to_referee)(applicant)
    web.sendmail(config.mail_sender, applicant.referee_email, subject, msg, headers = mail_headers)

def notify_applicant(applicant):
    subject = 'MLSS 2016: Reference Letter'
    msg = web.template.Template(msg_notify_applicant)(applicant)
    web.sendmail(config.mail_sender, applicant.email, subject, msg, headers = mail_headers)

def notify_referee(applicant):
    subject = 'MLSS 2016: Reference Letter Received'
    msg = web.template.Template(msg_notify_referee)(applicant)
    web.sendmail(config.mail_sender, applicant.referee_email, subject, msg, headers = mail_headers)

def resend_password(user):
    subject = 'MLSS 2016 - Password request'
    msg = web.template.Template(msg_resend_password)(user)
    web.sendmail(config.mail_sender, user.email, subject, msg, headers = mail_headers)

def firstmsg_to_admitted_applicant(applicant):
    subject = 'Admitted MLSS 2016 in Peru'
    msg = web.template.Template(first_msg_to_admitted_applicant)(applicant)
    web.sendmail(config.mail_sender, applicant.email, subject, msg, headers = mail_headers)

def paymsg_to_admitted_applicant(applicant):
    subject = 'Admitted MLSS 2016 in Peru - Payment'
    msg = web.template.Template(pay_msg_to_admitted_applicant)(applicant)
    web.sendmail(config.mail_sender, applicant.email, subject, msg, headers = mail_headers)

def to_rejected_applicant(applicant):
    subject = 'Rejected MLSS 2016 in Peru'
    msg = web.template.Template(msg_to_rejected_applicant)(applicant)
    web.sendmail(config.mail_sender, applicant.email, subject, msg, headers = mail_headers)

def firstmsg_to_attendee(applicant):
    subject = 'Welcome to the MLSS 2016 in Arequipa-Peru'
    msg = web.template.Template(first_msg_to_attendee)(applicant)
    web.sendmail(config.mail_sender, applicant.email, subject, msg, headers = mail_headers)

def secondmsg_to_attendee(applicant):
    subject = 'MLSS 2016 - Web updated'
    msg = web.template.Template(second_msg_to_attendee)(applicant)
    web.sendmail(config.mail_sender, applicant.email, subject, msg, headers = mail_headers)
