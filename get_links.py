import urllib2
link = 'http://www.gogo.mn'
page = urllib2.urlopen(link)
content = page.read()
print content
