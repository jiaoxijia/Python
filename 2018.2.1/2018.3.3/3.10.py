#coding:utf-8
# print "This propgram will calculate the area of triangle"
#
# a = 0
# h = 0
#
# area = 0.0
#
# a = input("请输入 a 的值：") #input 是一个输入函数
# h = input("请输入 h 的值：")
#
# area = 1.0 * a*h/2
# print "三角形的面积是："+ `area` #利用一对反引号可以将数字转换为字符串
#
# print "the area is :" +area.__str__()

#字符串的连接与倍增
# a = 'A'*5 + ' '+ "bb" #字符串能利用的算术运算符只有 + 和 *
# print a
import numpy as np
import re
import matplotlib.pyplot as plt
import pandas as pd
import urllib
data = pd.read_excel("filename.xlsx")#使用pandas 读取 excel
data1 = pd.read_csv("filename.csv",delimiter=';')#从scv中读取数据
data2 = urllib.request().urlopen().read()
dstr = data2.decode() #decode（）方法将data2转换成str格式
m = re.findall("正则表达式",dstr)

'''
数据清洗和整理：
数据整理
去空值 去重 合并 选取 数据准备
重要准备：index，headers，columns
'''
df = pd.DataFrame()
df.reindex #显示索引
df._combine_match_columns() #显示列名
df.values() #显示数据值

df.describe() #显示数据描述
df.isnull() #测试是否是空值
df.notnull() #测试空值
df.dropna(axis=1,how="all") #按列删除all Na ，缺省值为axis=0，按行删除Na
df.fillna()
#填充，inplace ，不产生副本
#fillna（0）填充0，fillna（{c1:v1,cx:vx}） 利用字典X列填充v
#可以利用函数：mean、random.randon等

#测试重值，返回True or False
df.duplicated()

#填充，inplace 不产生副本
#可利用['列名']列表，可以按列删除重复
#tack_last = True ,保留最后一个记录
df.drop_duplicates()
