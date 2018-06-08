import urllib2

req = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    response = urllib2.urlopen(req)

    print response.read()
except urllib2.HTTPError, e:
    print e.code
    print e.reason