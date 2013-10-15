import get_links
import Queue
import urllib2

class Crawler:
    def __init__(self):
        self.links = Queue.Queue()
        self.links.put('http://www.gogo.mn')

    def start(self):
        while self.links.empty() == False:
            link = self.links.get()
            self.visit_link(link)
            try:
                new_links = get_links.get_links(link)
                for l in new_links:
                    self.links.put(l)
            except:
                pass

    def visit_link(self, link):
        print link

crawler = Crawler()
crawler.start()
