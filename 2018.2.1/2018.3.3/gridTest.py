#!--*-- coding:utf-8--*--
import urllib
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.grid_search import GridSearchCV

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
# prepare a range of alpha values to test
alphas = np.array([1,0.1,0.01,0.001,0.0001,0])
# create and fit a ridge regression model,testing each alpha
model = Ridge()
grid = GridSearchCV(estimator=model,param_grid=dict(alpha = alphas))
grid.fit(x,y)
print grid
# summarize the results of the grid search
print grid.best_score_
print grid.best_estimator_.alpha