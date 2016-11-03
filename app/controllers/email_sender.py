# Author: Alex Ksikes

import web

from config import view
from web import form
from app.helpers import utils
from app.helpers import email_templates
from app.models import applicants
import time


def get_mail_to_send(option):
    if option == 'Admitted First Message':
        # send first email to admitted applicants
        context = "admitted"
        emailfun = email_templates.firstmsg_to_admitted_applicant
    elif option == 'Admitted Payment Message':
        # send payment email to admitted applicants
        context = "admitted"
        emailfun = email_templates.paymsg_to_admitted_applicant
    elif option == 'Rejected':
        # send email to rejected applicants
        context = "rejected"
        emailfun = email_templates.to_rejected_applicant
    elif option == 'Attendee First Message':
        # send email to attendees
        context = "attendee"
        emailfun = email_templates.firstmsg_to_attendee
    elif option == 'Attendee Second Message':
        # send email to attendees
        context = "attendee"
        emailfun = email_templates.secondmsg_to_attendee

    return context, emailfun


def send_emails(d):

    # clean up some fields
    utils.dict_remove(d, 'submit')
    # get context and email function
    context, emailfun = get_mail_to_send(d.group)

    results, num_results = applicants.get_applicants(
        context=context
    )

    if d.get('test_applicants', False):
        print("Sending to test applicants")
    else:
        print(("Sending to %i emails") % num_results)

    for i, applicant in enumerate(results):
        # send 50 emails then wait 15 sec
        if i != 0 and i % 50 == 0:
            time.sleep(15)

        # send to only test applicants
        if d.get('test_applicants', False):
            if "mlssTest_" not in applicant.first_name:
                continue

        emailfun(applicant)

        # send emails to rejected applicants
        print(i)
        print(applicant.email)
    return


class sender:

    def GET(self):

        return view.email_sender(self.form(),
                                 web.input(success='').success)

    def POST(self):

        f = self.form()
        if not f.validates(web.input(_unicode=False)):
            return view.email_sender(f)
        else:
            success = True
            try:
                send_emails(f.d)
            except:
                raise
                success = False
            raise web.seeother('/email_sender?success=%s' % success)

    def form(self):

        # vemail = form.regexp(r'.+@.+', 'Please enter a valid email address')

        return form.Form(
            form.Checkbox('test_applicants',
                          description='Send emails only to test applicants (mlssTest_)?',
                          value='1'),
            form.Dropdown('group',
                          ('', 'Admitted First Message',
                           'Admitted Payment Message',
                           'Rejected',
                           'Attendee First Message',
                           'Attendee Second Message'),
                          form.notnull,
                          description='Send template emails to'),
            form.Button('submit', type='submit', value='Send emails'),
        )
