#!--*--coding:utf-8--*--
import urllib2
import re
import os

print os.getcwd()
url = "file:movie_review.htm"
req = urllib2.Request(url,headers={'User-Agent':'Magic Browser'})
webpage= urllib2.urlopen(req)
# webpage = urllib2.urlopen(url)
html= webpage.read()

# fh = open('movie_review.htm')
# html = fh.read()
print html
Img = re.compile(r'src=".+?\.jpg"')
ImgList = re.findall(Img,html)
print ImgList

for img0 in ImgList:
    ls_img = img0.split("', '")