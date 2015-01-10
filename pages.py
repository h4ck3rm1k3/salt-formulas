import urllib2
import re
for x in xrange(1,15):
    url = 'http://saltstarters.org/browse/?page=%s' % x
    f = urllib2.urlopen(url)
    d = f.read()
    for u in re.findall(r'\>([^\<\>]+)\<\/a\>',d):
        if u.find('/') > -1 :
            print(u)
    
