#coding:UTF-8
import numpy as np
import urllib

# url with dataset
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
# download the file
raw_data = urllib.urlopen(url)

# print raw_data
# load the CSV file as a numpy matrix
dataset = np.loadtxt(raw_data,delimiter=",")
# separate the data from the target attributes
X = dataset[:,0:7]
y = dataset[:,8]

