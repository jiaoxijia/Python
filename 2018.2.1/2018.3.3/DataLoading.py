#!--*--coding:UTF-8--*--
import numpy as np
import urllib
from  sklearn import preprocessing
# url with dataset
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data'

# download the file
raw_data = urllib.urlopen(url)
#print(raw_data)
# load the CSV file as a numpy matrix
dataset = np.loadtxt(raw_data, delimiter=",")
# separate the data from the target attributes
x = dataset[:,0:7]   #特征矩阵
y = dataset[:,8]     #目标变量
# print(x,y)

#数据归一化（Data Normalization）

#normalize the data attributes
normalized_x = preprocessing.normalize(x)
# standardize the data attributes
standradized_x = preprocessing.scale(x)

#特征选择（Feature Selection) 下面的树算法（Tree algorithms）计算特征的信息量
from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier
model = ExtraTreesClassifier()
model.fit(x,y)
#display the relative importance of each attribute
print model.feature_importances_

# #逻辑回归 算法优点是可以给出数据所在类别的概率
# from sklearn import metrics
# from sklearn.linear_model import LogisticRegression
# model = LogisticRegression()
# print model
# # make predictions
# expected = y
# predicted = model.predict(x)
# # summarize the fit of the model
# print metrics.classification_report(expected,predicted)
# print metrics.confusion_matrix(expected,predicted)

#朴树贝叶斯 著名的机器学习算法，该方法的任务是还原训练样本数据的分布密度，其在多类别中有很好的效果

# from sklearn import metrics
# from sklearn.naive_bayes import GaussianNB
#
# model = GaussianNB()
# model.fit(x,y)
# print model
#
# # make predictions
# expected = y
# predicted = model.predict(x)
#summarize the fit of the model
# print metrics.classification_report(expected,predicted)
# print metrics.confusion_matrix(expected, predicted)


#K近邻算法 通常被用作是分类算法的一部分，比如可以用来评估特征，在特征选择上可以用的K近邻算法
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
#fit sklearn.neighbor model to the data
model = KNeighborsClassifier()
model.fit(x,y)
print model

#make predictions
expected = y
predicted = model.predict(x)
# summarize the fit of the model
print metrics.classification_report(expected, predicted)
print metrics.confusion_matrix(expected, predicted)


#决策树 分类与回归树（Classification and Regression Trees, CART)算法常用于特征含有类别信息的分类或者回归问题
# ，这种方法适用于多分类情况
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
# fit a CART model to the data
model = DecisionTreeClassifier()
model.fit(x,y)
print model
# make predictions
expected = y
predicted = model.predict(x)















