import re
# 线性运算
import numpy as np

# 数据处理
import pandas as pd

# 数据可视化
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import style

# 算法
# Algorithms
from sklearn import linear_model #线性模型
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier #随机森林
from sklearn.linear_model import Perceptron #感知器
from sklearn.linear_model import SGDClassifier #随机梯度下降
from sklearn.tree import DecisionTreeClassifier #决策树分类器
from sklearn.neighbors import KNeighborsClassifier #K-近邻分类器
from sklearn.svm import SVC,LinearSVC #线性SVC
from sklearn.naive_bayes import GaussianNB #高斯朴素贝叶斯


import warnings
warnings.filterwarnings('ignore')
# from IPython import get_ipython
# get_ipython().run_line_magic('matplotlib','inline')

# %matplotlib inline

train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')

train_df['Survived'].value_counts().plot.pie(autopct='%1.2f%%')
# print(train_data.head())
# print(test_data.head())
# train_data.info()
# print("-" * 40)
# test_data.info()
# print(train_df['Survived'].value_counts().plot.pie(autopct='%1.2f%%'))

# print(train_df.describe())

# 统计缺失值

total = train_df.isnull().sum().sort_values(ascending=False)
# print(total)
percent_1 = train_df.isnull().sum()/train_df.isnull().count()*100
# print(percent)
# 计算缺失值的百分比，大致判断处理的复杂度，以及该数据是否有用的必要
percent_2 = (round(percent_1,1).sort_values(ascending=False))# 降序排列
# print(percent_2)
missing_data = pd.concat([total,percent_2], axis=1, keys=['Total','%']) #连接函数
# print(missing_data)
# print(missing_data.head(5))

train_df['Survived'].value_counts().plot.pie(autopct = '%1.2f%%')

"""
分析各个变量与生存率之间的关系
例如：Sex 和 Age
"""
# survived = 'survived'
# not_survived = 'not survived'
# fig,aexs = plt.subplot(nrows = 1,ncols = 2,figsize =(10,4)) #一行两列 两个图
# women = train_df[train_df['Sex']=='female']
# men = train_df[train_df['Sex']=='male']
# ax = sns.distplot(women[women['Survived']==1].Age.dropna(),bins=18,label=survived,ax = aexs[0],kde=False)































