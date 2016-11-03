# Author: Alex Ksikes

import web

from config import view
from web import form
from app.helpers import utils
from app.helpers import email_sending
from app.models import applicants


def send_emails(d):

    # clean up some fields
    utils.dict_remove(d, 'submit')
    # get admitted applicants
    if (d.group == 'Admitted First Message' or
       d.group == 'Admitted Payment Message'):
        context = "admitted"
    elif d.group == 'Rejected':
        context = "rejected"
    # elif d.group == 'Pending':
    #     context = "pending"
    # elif d.group == 'All':
    #     context = "all"

    # Admitted who receive scholarships must be in Pending
    # they will be handled separately

    results, num_results = applicants.get_applicants(
        context=context
    )
    print(("Sending to %i emails") % num_results)
    for applicant in results:
        # send emails to selected applicants
        email_sending.to_applicant(applicant, d.subject, d.body)
        print(applicant.email)
    return


class sender:

    def GET(self):

        return view.personalized_email_sender(self.form(),
                                 web.input(success='').success)

    def POST(self):

        f = self.form()
        if not f.validates(web.input(_unicode=False)):
            return view.personalized_email_sender(f)
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
                          ('', 'Admitted',
                           'Rejected',
                           'Scholarship recipients'),  # 'Pending', 'All'),
                          form.notnull,
                          description='Send emails to'),
            form.Textbox('subject',
                form.notnull,
                description='Subject',
                pre='<label class="help">E.g. [MLSS16] Decision Notification</label>'),
            form.Textarea('body',
                form.notnull,
                description='Body',
            pre="<label class='help'>Take into account that it only the body, the full message starts with 'Dear ApplicantName, ...' and ends with 'Best wishes, ...' </label>"),
            # form.Dropdown('email_template',
            #               ('', 'msg_to_admitted_applicant', 'msg_to_applicant',
            #                'msg_to_applicant_simple', 'msg_notify_applicant'),
            #               form.notnull,
            #               description='Email template'),
            # form.Textbox('subject',
            #              form.notnull,
            #              description='Subject'),
            # form.Textarea('email_body',
            #               form.notnull,
            #               description='Email body'),
            form.Button('submit', type='submit', value='Send emails'),
        )
