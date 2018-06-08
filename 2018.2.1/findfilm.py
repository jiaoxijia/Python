import urllib2
import re
import os
url = 'http://theater.mtime.com/China_Beijing/'
req = urllib2.Request(url,headers={'User-Agent':'Magic Browser'})
webpage= urllib2.urlopen(req)
strw= webpage.read()
# print strw
# tg_strw=strw.find('hotplaySvList = []')
tg_strw = re.match(r"([\w\W]*)",strw)
print tg_strw
if tg_strw == -1:
    print 'not find start tag'
    os._exit()
# tmp=strw[tg_strw:-1]
# tg_end=tmp.find(':')
# if tg_end== -1:
#     print 'not find end tag'
#     os._exit()
# tmp=tmp[len('hotplaySvList = []:tg_end')]