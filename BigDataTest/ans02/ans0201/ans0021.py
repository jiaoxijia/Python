#coding:utf-8
import pandas as pd
import numpy as np

name = []
s_time = []
e_time = []
bor = []
col = ['电影名称','上映日期','结束放映日期','票房']

f = open(r"C:\PythonProgram\BigDataTest\task0201\spider.log")
# print f.read()

for line in f:
    if "http://www.movie.com/bor/" in line:
        name.append(line.split(",")[2].split(';')[0])
        s_time.append(line.split(',')[2].split(';')[1])
        e_time.append(line.split(',')[2].split(';')[2])
        bor.append(line.split(',')[2].split(';')[0].split(';'))
        #字段选取看数据行的歌声进行切割，过于混乱的数据会加以判断
d = dict(zip(col,[name,s_time,e_time,bor]))

print d
df = pd.DataFrame(d)
df = df.drop_duplicates()
df.to_csv('ans0021.csv',index=False,columns=col,encoding='utf_8_sig')