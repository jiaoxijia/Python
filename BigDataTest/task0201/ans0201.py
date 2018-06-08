#coding:utf-8
import re
import pandas as pd

data = open('spider.log')
line = data.readline()
movie = []
starttime = []
endtime = []
score = []

#筛选电影数据,加入字段
while line:
    line=data.readline()
    if 'http://www.movie.com/dor/' in line:
        # print line
        ls = line.split(';')
        starttime.append(ls[1])
        endtime.append(ls[2])
        movie.append(ls[0].split(',')[2])
        score.append(re.sub('票房（万）','',ls[7]))

# 转换文件类型
datas = pd.DataFrame({u'电影名称':movie,u'上映时间':starttime,u'结束时间':endtime,u'票房(万元)':score})
# print datas.select
# 去除重复数据，从新定义索引
datas = datas.drop_duplicates()
datas.to_csv('dat0201.csv',sep=',',index=False,encoding='utf-8')
print datas