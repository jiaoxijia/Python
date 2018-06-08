#coding:utf-8
import pandas as pd

# print(pd.__version__)
arr=[1,2,3,4,5]
s1=pd.Series(arr)
# print(s1)

# 从Ndarry创建 Series
import numpy as np
n=np.random.randn(5) # 创建一个随机 Ndarry数组
index = ['a','b','c','d','e']
s2 = pd.Series(n,index=index)
# print(s2)

# 从字典创建Series
d={'a':1,"b":2,"c":3,"d":4,"e":5}
s3=pd.Series(d)
# print(s3)

# Series基本操作
# 修改索引
# print(s1)
s1.index=['A','B','C','D','E'] #修改后的索引
# print(s1)

# 纵向拼接
s4=s3.append(s1) #纵向加上几行
# print(s4)

# 按索引删除指定元素
# print(s4)
s4=s4.drop('e')
# print(s4)

# 修改指定元素
s4['A'] = 6 # 删除索引为A的值 = 6 将索引A的值换为6
# print(s4)

# 按指定索引查找元素
# print(s4['B'])

# 切片操作
# print(s4[:3]) #提S4中取前3个值

#Series 运算
# 加法运算 (Series加法运算按照索引计算，若索引不同则填充为NaN值)
# print(s4.add(s1))

#Series 减法运算(按照索引进行计算，若不同则填充为NaN值)
# print(s4.sub(s3))

# Series 乘法运算(按照索引进行计算，索引不同则填充为空值（NaN）)
# print(s4.mul(s3))

# Series 除法运算
# print(s4.div(s3))

# 求平均值
# print(s4.median())

# Series求和
# print(s4.sum())

# Series 求最小值
# print(s4.min())

# 创建DataFrame 数据类型
'''
DataFrame 与 Series不同
DataFrame 可以存在多列数据
所以，一般情况下DataFrame更长用

'''
# 通过NumPy创建DataFrame
dates = pd.date_range('today',periods=6) #定义时间为index
num_arr = np.random.randn(6,4) #传入 numpy随机数组
columns=['A','B','C','D'] #将列表作为列名
df1 = pd.DataFrame(num_arr,index=dates,columns=columns)
# print(df1)
# print(dates)

#通过字典创建数组 DataFrame
data = {'animal':['cat','cat','snake','dog','dog','dog','cat','snake','cat','dog'],
        'age':[2.5,3,0.5,np.nan,5,2,4.5,np.nan,7.3,10],
        'visits':[1,3,2,3,2,3,1,1,2,1],
        'priority':['yes','yes','no','yes','no','no','no','yes','no','no']
        }
labels = ['a','b','c','d','e','f','g','h','i','j']
df2 = pd.DataFrame(data,index=labels)
# print(df2)
print(df2.dtypes)