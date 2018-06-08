#coding:utf-8
import sys
sys.path.append("...文件路径...")
import KNN
from numpy import *

dataSet,labels = KNN.createDataSet()
input = array([1.1,0.3])
k = 3
output = KNN.classify(input, dataSet,labels,k)
print "测试数据为：",input,"分类结果为：",output

