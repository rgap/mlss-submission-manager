## EDITED BY: rgap

class other:
    def GET(self, url):
        # if url == '/sitemap.xml':
        #     fh = open('sitemap.xml')
        #     sitemap = fh.read()
        #     fh.close()
        #     return sitemap
        if url == '/robots.txt':
            fh = open('robots.txt')
            robots = fh.read()
            fh.close()
            return robots

