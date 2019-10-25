
from plone import api
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from BeautifulSoup import BeautifulSoup
import urllib2
import re
import time

class LinkCheckerView(BrowserView):

    template = ViewPageTemplateFile('linkchecker_view.pt')
    
    def __call__(self):
        page_url = self.context.absolute_url().replace('/utility_linkchecker','')
        response = None
        self.links = []
        
        # Get page
        try:
            response = urllib2.urlopen(page_url, timeout = 5)
            soup = BeautifulSoup(response)
            div = soup.find("div", {"id" : "content-container"})
            if div:
                for link in div.findAll('a'):
                    if link:
                        if not link.startswith('#') or not link.startswith('/') or not link.startswith('tel:') or not link.startswith('mailto:'):
                            self.links.append({
                                'url': link.get('href'),
                                'status': 0,
                                'message': "UNKNOWN: Utility failed...",
                                'style': "unknown",
                            })
            response.close()
        except urllib2.URLError, e:
            try: 
                response.close()
            except:
                pass
            raise Exception("ERROR: Connection Issue")


        # Check links
        for link in self.links:
            response = None
            try:
                response = urllib2.urlopen(link['url'], timeout = 5)
                link['status'] = response.code
                if response.code == 200:
                    link['message'] = "PASSED"
                    link['style'] = "pass"
                elif response.code == 301:
                    link['message'] = "WARNING: Possible change"
                    link['style'] = "warn"
                elif response.code == 302:
                    link['message'] = "WARNING: Possible change"
                    link['style'] = "warn"
                elif response.code == 303:
                    link['message'] = "WARNING: Possible change"
                    link['style'] = "warn"
                elif response.code == 307:
                    link['message'] = "WARNING: Possible change"
                    link['style'] = "warn"
                else:
                    link['message'] = "ERROR: Connection issue"
                    link['style'] = "error"
                response.close()
            except urllib2.URLError, e:
                link['status'] = 408
                link['message'] = "ERROR: Connection issue"
                link['style'] = "error"
                try: 
                    response.close()
                except:
                    pass


        


        return self.template()




    @property
    def portal(self):
        return api.portal.get()
        