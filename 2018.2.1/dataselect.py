#coding:utf-8

#pandas中数据的选取
import sys
import re
import urllib2
import os
import numpy as np
import pandas as pd
import matplotlib as mpt
import face_recognition_models as frm


dates = pd.date_range("20170101",periods=6)
col = ['A','B','C','D']     #列名

df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=col)

# print df

# print df['D']     #选取一列数据
# print df.D        #选取一列数据
col = ['A','B','D']
# print df[col]     #选取多行数据
# print df['20170102':'20170104']     #选取多行数据

#loc pandas中使用标签选取数据，
# 下面是根据标签名字选取某一行或者所有行数据，，然后选取其中某一列或者几列数据
# print df.loc['20170102']    #根据index的名称来选取一行数据
# print df.loc[:, ['B', 'D', 'C']]    #选取BDC列所有数据
# print df.loc['20170102',['A','D']]  #选取20170102行的A、D两列数据

#ix 混合选择,选择'A'和'C'的两列，并选择前三行数据。
# print df.ix[:3, ['A', 'C']]

# print df.A >10          #判断A列中大于10的数据，返回值是Boolean类型
# print df[df.A > 10]     #选取A列中数据大于10的项

# print df[df.A.notnull()]    #选取A列不为空的数据

# df[['A','D','C','B']].to_csv('dataselect.csv')

print df.__doc__