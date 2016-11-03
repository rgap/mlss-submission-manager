# Author: Alex Ksikes 

import web
import config

from app.models import applicants
from config import view
from web import form

def update_applicant(applicant, d):

    print(applicant.id)
    print(d.first_name)
    applicants.update_applicant(applicant.id,
                                d.document_id,
                                d.first_name,
                                d.last_name)
    return

class info:
    def GET(self, secret_md5):
        applicant = applicants.get_by_secret_md5(secret_md5)
        
        if not applicant and secret_md5 == '0' * 32:
            applicant = applicants.get_dummy_record()
        
        return view.admitted_form(self.form(applicant), applicant, web.input(success='').success)
    
    def POST(self, secret_md5):
        applicant = applicants.get_by_secret_md5(secret_md5)
        
        f = self.form(applicant)
        if not f.validates(web.input(_unicode=False)):
            return view.admitted_form(f, applicant)
        else:
            success = True
            try:
                update_applicant(applicant, f.d)
            except:
                raise
                success = False
            raise web.seeother('/submit_admitted/%s?success=%s' % (secret_md5, success))
    
    def form(self, applicant):

        # vemail = form.regexp(r'.+@.+', 'Please enter a valid email address')

        return form.Form(
            form.Textbox('document_id',
                         form.notnull,
                         value=applicant.document_id,
                         description='Passport number or DNI if Peruvian'),
            form.Textbox('first_name',
                         form.notnull,
                         value=applicant.first_name,
                         description='Your first Name'),
            form.Textbox('last_name',
                         form.notnull,
                         value=applicant.last_name,
                         description='Your last Name'),
            # form.Textbox('email',
            #              form.notnull, vemail,
            #              value=applicant.email,
            #              description='Email we use to communicate with you'),
            form.Button('submit', type='submit', value='Update info'),
        )
