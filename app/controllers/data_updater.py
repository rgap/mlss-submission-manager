# Author: Alex Ksikes

import web

from config import view
from web import form
import csv
from app.models import applicants


def load_file(file_csv):

    f = file_csv.file  # Or use a file(-like) object
    try:
        reader = csv.reader(f)
        headers = reader.next()
        column = {}
        for h in headers:
            column[h] = []
        for row in reader:
            for h, v in zip(headers, row):
                column[h].append(v)
        for i in range(0, len(column['email'])):
            print(column['email'][i])
            print(column['username'][i])
            print(column['password'][i])
            applicants.update_applicant_user(column['email'][i],
                                             column['username'][i],
                                             column['password'][i])

    finally:
        f.close()


class updater:

    def GET(self):

        return view.data_updater(self.form(),
                                 web.input(success='').success)

    def POST(self):

        f = self.form()
        file_csv = web.input(file_csv={}).file_csv

        if file_csv == '' or file_csv.filename == '':
            return view.data_updater(f)
        else:
            success = True
            try:
                load_file(file_csv)
            except:
                raise
                success = False
            raise web.seeother('/data_updater?success=%s' % success)

    def form(self):

        return form.Form(
            form.File('file_csv',
                      form.notnull,
                      description='CSV File'),
            form.Button('submit', type='submit', value='Send emails'),
        )
