#coding=utf-8
import pandas as pd

name=[]
s_time=[]
e_time=[]
bor=[]
col=['电影名称','上映日期','结束放映日期','票房']

with open('D:/arg/task0201/spider.log') as f:
    for line in f:
        if 'http://www.movie.com/bor/' in line:
            name.append(line.split(',')[2].split(';')[0])
            s_time.append(line.split(',')[2].split(';')[1])
            e_time.append(line.split(',')[2].split(';')[2])
            bor.append(line.split(',')[2].split(' ;')[0].split(';')[-1])
            #字段选取看数据行的格式进行切割，过于混乱的数据会加判断
d = dict(zip(col,[name,s_time,e_time,bor]))

df = pd.DataFrame(d)
df = df.drop_duplicates()
df.to_csv('ans0201.csv',index=False,columns=col,encoding='utf_8_sig')
