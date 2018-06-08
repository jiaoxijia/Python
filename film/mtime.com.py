import urllib2
import re

url="http://www.mtime.com/top/movie/top100/"
headers={'User-Agent':'Mozilla/5.0'}
req=urllib2.Request(url,headers=headers)
html=urllib2.urlopen(req).read()

#print html
div=str(r'<div class="top_list"> ')

