import urllib2
import re
import os

url='http://theater.mtime.com/China_Beijing/'#1ans：http://theater.xtime.com/ Beijing/
req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})#2ans：url
webpage= urllib2.urlopen(req)
strw=webpage.read()
tg_start=strw.find('hotplaySvList = [']
if tg_start==-1:
	print 'not find start tag'
	os.exit()
tmp=strw[tg_start:-1]
tg_end=tmp.find(';')
if tg_end==-1 :
	print 'not find end tag'
	os.exit()
tmp= tmp[len(' hotplaySvList = [']:tg_end)
tar_ls=tmp.split("},{")#3ans：},{
dict_film={}#4ans：{}
for t0 in tar_ls:
	ls_t=t0.split(',')
	id=ls_t[0].split(':')[-1].strip()#5ans：-1
	film=ls_t[-1].split('"')[-2].strip()#6ans：split
	dict_film[id]=film #7ans：dict_film
for t in dict_film:
	print "id: "+t+"  film:  "+dict_film[t]
print 'ok  total : '+`len(dict_film)`

