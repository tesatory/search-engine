import urllib2
from HTMLParser import HTMLParser

class LinkParser(HTMLParser):
    links = list()
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    self.links.append(attr[1])
                
def get_links(url):
    page = urllib2.urlopen(url)
    content = page.read()
    parser = LinkParser()
    parser.feed(content)
    return parser.links

#print get_links('http://www.gogo.mn')
