#coding=utf-8
import numpy as np
import urllib2
import re
rate=[]
#urllib2方式
uri  = 'file:///D:/arg/task0202/movie_review.htm'
req = urllib2.Request(uri)  #urllib2是网页访问啊，uri是绝对资源路径
res = urllib2.urlopen(req)
html = res.read()
s = html.find('正在上映')
e = html.find('即将上映')
temp=html[s:e]

result=re.findall('<span class="subject-rate">(.*?)</span>',temp)
for r in result:
    r = r.replace(' ','')
    rate.append(float(r))

avg = np.mean(rate)

with open('ans0202.txt','w') as f:
    f.write('%.4f'%avg)
#文件方式访问
# with 语句，不管在处理文件过程中是否发生异常，都能保证 with 语句执行完毕后已经关闭了打开的文件句柄
# with open('D:/arg/task0202/movie_review.htm') as f:
#     html = f.read()
#     s = html.find('正在上映')
#     e = html.find('即将上映')
#     temp = html[s:e]
#     result =re.findall('<span class="subject-rate">(.*?)</span>',temp)
#     for r in result:
#         r = r.replace(' ','')
#         rate.append(float(r))
#
# avg = np.mean(rate)
# with open('ans0202.txt','w') as f:
#     f.write('%.4f'%avg)
#
