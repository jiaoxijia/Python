#!coding=utf-8
"""
Author zll
Datatime 2018.3.9
通过使用sklearn ，简要学习机器学习
"""

# --*--coding：UTF-8--*--

'''
:returns
df

df

'''

# a = 'aa'*10 +"\n"+"bbb\t"*10
# print a
#
# a = raw_input()
# print a

# a = 123
# b = 456
#
# c =a + b
# d = "a connect b =>"+`a`+`b`
# print a
# print b
# print c
# print d

# def aaa(a,b):
#     ab = 0
#     if a >b :
#         pass
#         ab = a *b/2
#     elif a< b:
#         ab = a+b
#
#     else:
#          print "我不知道你输入的是什么"
#     return ab
#
# print aaa(5, 5)
# a = "   aa, bb, cc   "
# print a.replace("",' ')
# print a.split(',')

tup = [] #定义一个元组
lis = () #定义一个list
dic = {} #定义一个字典
k = 30
dic[`k`] = [11,22,33,44,55,66]
k=k+ 1
print dic.get(`k`)
k = k-1
print dic.get(`k`)

words="""#-blue-蓝⾊（的）
u #-green-绿⾊（的）
 u #-red-红⾊（的）
  u #-yellow-⻩⾊（的）
   u #-orange-橘⾊（的）
    u #-purple-紫⾊（的）
     u #-white-⽩⾊（的）
      u #-black-⿊⾊（的）
       u #-brown-棕⾊（的）"""
import os

print os.getcwd()
path = "C:\\AppData"
print os.listdir(path)