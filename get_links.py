import urllib2
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    print attr[1]
                

link = 'http://www.gogo.mn'
page = urllib2.urlopen(link)
content = page.read()
parser = MyHTMLParser()
parser.feed(content)

