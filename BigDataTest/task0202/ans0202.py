#coding:utf-8
import re
import pandas as pd
import urllib2
# # 数据导入
op = open("movie_review.htm",'r')
html = op.read()

a = ''
# 数据筛选
data = re.findall(r'<div class="mod-bd">(.*?)</div>',html,re.S)
a = a.join(data)
print a

op.close()