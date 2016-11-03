#!/usr/bin/env python
# Author: Alex Ksikes 

# TODO:
# - in list view show that some comments have been left
# - cut_length with more less and tooltip
# - each grader could be assigned a unique color. His actions will then be stamped by their chosen color.
# - sessions do not clean up because of is_logged var
# - let users remove their ratings
# - very weird, lighttpd refuses mod_auth on urls of the type /application/

import web
import config
import app.controllers

from app.helpers import session

urls = (
    # CLOSED
    '/submit_application',                       'app.controllers.submit_application.apply',
    # '/submit_application',                       'app.controllers.submit_application.closed',
    # CLOSED
    '/submit_reference/([0-9a-f]{32})',          'app.controllers.submit_reference.refer',
    # '/submit_reference/.*',          'app.controllers.submit_reference.closed',

    '/submit_admitted/.*',          'app.controllers.submit_admitted.info',
    '/email_sender',          'app.controllers.email_sender.sender',
    '/personalized_email_sender',          'app.controllers.personalized_email_sender.sender',


    '/data_updater',          'app.controllers.data_updater.updater',


    ## EDITED BY: rgap
    #'/affiliated/submit_application',            'app.controllers.submit_application.apply_simple',
    
    '/(|new|pending|all|admitted|attendee|scholarship_recipient)',              'app.controllers.browse.list',
    '/(search|rejected|reviewed)',               'app.controllers.browse.list',
    '/applicant/(\d+)',                          'app.controllers.browse.show',
    
    '/admit',                                    'app.controllers.actions.admit',
    '/reject',                                   'app.controllers.actions.reject',
    '/undecide',                                 'app.controllers.actions.undecide',
    '/make_attendee',                            'app.controllers.actions.make_attendee',
    '/rate',                                     'app.controllers.actions.rate',
    
    '/applicant/(\d+)/comment',                  'app.controllers.actions.comment',
    '/delete_comment/(\d+)',                     'app.controllers.actions.delete_comment',
    
    '/grant/(\d+)',                              'app.controllers.actions.grant',
    
    '/account',                                  'app.controllers.account.index',
    '/account/register',                         'app.controllers.account.register',
    '/account/login',                            'app.controllers.account.login',
    '/account/logout',                           'app.controllers.account.logout',
    '/account/resend_password',                  'app.controllers.account.resend_password',
    '/account/help',                             'app.controllers.account.help',
    
    '/settings',                                 'app.controllers.settings.index',
    '/settings/change_nickname',                 'app.controllers.settings.change_nickname',
    '/settings/change_password',                 'app.controllers.settings.change_password',
    '/settings/change_email',                    'app.controllers.settings.change_email',
    
    '/(?:img|js|css|resumes|tutorial)/.*',                        'app.controllers.public.public',

    '/tests/session',                            'app.tests.session',
    '/tests/upload',                             'app.tests.upload',
    '(.+)',                                             'app.controllers.others.other',
)


app = web.application(urls, globals())

if web.config.email_errors:
    app.internalerror = web.emailerrors(web.config.email_errors, web.webapi._InternalError)
session.add_sessions_to_app(app)

if __name__ == "__main__":
    app.run()
