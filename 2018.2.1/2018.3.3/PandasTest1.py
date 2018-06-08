#！--*--coding:utf-8--*--
import pandas as pd
from pandas import Series,DataFrame
import numpy
import numpy as np
from pandas import Index
# print '使用字典生成DataFrame，key为列名字'
# data = {'state':['ok','ok','good','bad'],
#         'year':[2000,2001,2002,2003],
#         'pop':[3.7,3.6,2.4,0.9]
#         }
# print DataFrame(data)#行索引默认为0,1,2,3
# #指定列索引为columns，不匹配的列为NaN
# print DataFrame(data,columns= ['year','state','pop','debt'])
df = pd.read_csv('film_log3.csv',sep=";")
print df
# print '指定行索引index'
# x = DataFrame(data,
#               columns= ['year','state','pop','debt'],
#               index= ['one','two','three','four'])
# print  x
#
# print '获取Index对象'
# x = Series(range(3),index= ['a','b','c'])
# index = x.index
# print index
#
# print '判断列，行索引是否存在'
# data= {'pop':{2,2.9},
#        'year':{20,2002}}
# x = DataFrame(data)
# print x
#
# print 'pop' in x.columns # True
# print  1 in x.index #True
#
# print 'Series根据行索引删除行'
# x = Series(numpy.arange(4),index= ['a','b','c','d'])
# print x.drop(['a','b'])

# pd.read