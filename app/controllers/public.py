# Author: Alex Ksikes 

import web
import mimetypes
#from app.helpers import session

class public:
    #@session.login_required
    def GET(self): 
        public_dir = 'public'
        try:
            file_name = web.ctx.path.split('/')[-1]
            web.header('Content-type', mime_type(file_name))
            utf_string = web.ctx.path.encode('utf-8')
            return open(public_dir + utf_string, 'rb').read()
        except IOError:
            raise web.notfound()

            
def mime_type(filename):
    return mimetypes.guess_type(filename)[0] or 'application/octet-stream' 
