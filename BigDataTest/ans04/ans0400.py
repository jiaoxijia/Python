#-*- coding:utf-8 -*-
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn import cross_validation
import pandas as pd
import numpy as np
import sys,re
reload(sys)
sys.setdefaultencoding("utf-8")
from  matplotlib.pylab import *
from pandas import Series
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

data = pd.read_csv(u'D:\\安徽赛项说明会\\样题\\arg\\arg04\\film-csv.txt',delimiter=';',names=[u'电影名称', u'上映时间', u'闭映时间', u'出品公司', u'导演', u'主角', u'影片类型', u'票房/万',
       u'评分', u'Unnamed: 9'],header=0,usecols=[0,4,5,6,7,8])
data = data.fillna(data.mean()).dropna(how='any',axis=0).drop_duplicates().reset_index()
print "大众的评分的最大值是:%.2f"%np.max(data[u'评分'])
print "大众的评分的最小值是:%.2f"%np.min(data[u'评分'])
print "大众的评分的中位数是:%.2f"%np.median(data[u'评分'])
print "大众的评分的平均数是:%.2f"%np.mean(data[u'评分'])

#定义函数处理数据
def SplitMark(values):
    values = re.sub(' |）|电影（| ','',values)
    word = re.split('/|、|,|，|',values)
    return word
def SplitLong(values):
    li = []
    for i in values:
        if len(i) > 9:
            for j in range(0,len(i),6):
                li.append(i[j:j+6])
        elif i == "":
            del i
        else:
            li.append(i)
    return li
data[u'影片类型'] = data[u'影片类型'].map(SplitMark)
data[u'影片类型'] = data[u'影片类型'].map(SplitLong)
data[u'导演'] = data[u'导演'].map(SplitMark)
data[u'主角'] = data[u'主角'].map(SplitMark)

#影片类型和票房得关系
Types_A = []
Bor_A = []
for i in range(len(data[u'影片类型'])):
    for ty in data[u'影片类型'][i]:
        Types_A.append(ty)
        Bor_A.append(data[u'票房/万'][i])
Type_bor = pd.concat([Series(Types_A,name='Type'),Series(Bor_A,name='票房/万')],axis=1).groupby("Type").sum().sort_values('票房/万')
#绘图1
fig = plt.figure(figsize=(12,8))
plt.subplots_adjust(bottom=0.1,top=0.9,hspace=0.6)
plt.tight_layout()
ax1 = plt.subplot(3,1,1)
Type_bor.tail(15).plot(kind='bar',ax=ax1,color='red',title=u'影片类型和票房的关系',rot=35)
# plt.savefig("TyB.jpg")
#导演和票房的关系
Leader_B = []
Bor_B = []
for i in range(len(data[u'导演'])):
    for le in data[u'导演'][i]:
        Leader_B.append(le)
        Bor_B.append(data[u'票房/万'][i])
Leader_bor = pd.concat([Series(Leader_B,name='Leader'),Series(Bor_B,name='票房/万')],axis=1).groupby("Leader").sum().sort_values('票房/万')
#绘图
ax2 = plt.subplot(3,1,2)
Leader_bor.tail(15).plot(kind='bar',ax=ax2,color='blue',title=u'导演和票房的关系',rot=30)
# plt.savefig("LeB.jpg")

#导演和类型之间的关系
Leader_C = []
Type_C = []
for i in range(len(data[u'导演'])):
    for le in data[u'导演'][i]:
        for ty in data[u'影片类型'][i]:
            Leader_C.append(le)
            Type_C.append(ty)
ax3 = plt.subplot(3,1,3)
plt.grid()
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)
plt.scatter(Leader_C[:60],Type_C[:60],color='green',label=u'票房/万')
plt.title(u'导演和类型之间的关系')
# fig.autofmt_xdate()
plt.legend()
# plt.savefig("LeTp.jpg")
plt.show()

#得到导演  类型 和主角这些数据
Leader_D = []
Type_D =[]
Actor_D = []
Movie_D = []
for i in range(len(data[u'导演'])):
    for le in data[u'导演'][i]:
        for ty in data[u'影片类型'][i]:
            for ac in data[u'主角'][i]:
                Leader_D.append(le)
                Type_D.append(ty)
                Actor_D.append(ac)
                Movie_D.append(data[u'电影名称'][i])
#将数据进行序列化  为数据预测做数据准备
Leader_S = list(set(Leader_D))
Leader_S.sort(key=Leader_D.index)
Leader_N = np.arange(len(Leader_D))
Dict1 = {}
for i in range(len(Leader_S)):
    for j in range(len(Leader_D)):
        if Leader_S[i] == Leader_D[j]:
            Dict1[i+1] = Leader_D[j]
            Leader_N[j] = i+1

Type_S = list(set(Type_D))
Type_S.sort(key=Type_D.index)
Type_N = np.arange(len(Type_D))
Dict2 = {}
for i in range(len(Type_S)):
    for j in range(len(Type_D)):
        if Type_S[i] == Type_D[j]:
            Dict2[i+1] = Type_D[j]
            Type_N[j] = i+1

Actor_S = list(set(Actor_D))
Actor_S.sort(key=Actor_D.index)
Actor_N = np.arange(len(Actor_D))
Dict3 = {}
for i in range(len(Actor_S)):
    for j in range(len(Actor_D)):
        if Actor_S[i] == Actor_D[j]:
            Dict3[i+1] = Actor_D[j]
            Actor_N[j] = i+1
fn = pd.DataFrame({
    'Leader_D':Leader_D,
    'Leader_N':Leader_N,
    'Type_D':Type_D,
    'Type_N':Type_N,
    'Actor_D':Actor_D,
    'Actor_N':Actor_N,
    'Movie_D':Movie_D,
})
#预测数据的演员：邓超 导演：周星驰 类型:喜剧
#得到对应的序列数
actor_num = fn.query('Actor_D=="邓超"').reset_index()['Actor_N'][0]
leader_num = fn.query('Leader_D=="周星驰"').reset_index()['Leader_N'][0]
type_num = fn.query('Type_D=="喜剧"').reset_index()['Type_N'][0]
#Xtrain
train = []
for i in range(len(Type_N)):
    train.append([Leader_N[i],Type_N[i],Actor_N[i]])
train = np.array(train)

IDs = [1231,1086,1184,1236,1050]
ID_data = pd.read_csv(u'D:\\安徽赛项说明会\\样题\\arg\\arg04\\score.log')
ScoreAll = []
for ID in IDs:
    data_score = ID_data.query(u'userid==%s'%ID).reset_index()
    trainX = []
    trainY = []
    for i in range(len(data_score[u'film'])):
        for j in range(len(Movie_D)):
            if data_score[u'film'][i].strip() == Movie_D[j].strip():
                trainX.append(train[j])
                trainY.append(data_score[u'score'][i])
    Xtrain =np.array(trainX)
    Ytrain = np.array(trainY)
    X_train,X_test,y_train,y_test = cross_validation.train_test_split(Xtrain,Ytrain,test_size=0.25,random_state=1)

    #预测
    regr = DecisionTreeRegressor(max_depth=8)
    # regr = GradientBoostingRegressor()
    regr.fit(X_train,y_train)
    print "train  score:",regr.score(X_train,y_train)
    print "test  score:",regr.score(X_test,y_test)
    print "="*10
    Rate = regr.predict([[leader_num,type_num,actor_num]])[0]
    if Rate > 10:
        Rate = 10
    elif Rate < 0:
        Rate = 0
    ScoreAll.append(Rate)
print
print "预测的评分的最大值是:%.2f"%np.max(ScoreAll)
print "预测的评分的最小值是:%.2f"%np.min(ScoreAll)
print "预测的评分的中位数是:%.2f"%np.median(ScoreAll)
print "预测的评分的平均数是:%.2f"%np.mean(ScoreAll)
with open('ans0400.dat','w') as f :
    dt ="%.2f"%np.max(ScoreAll)+","+"%.2f"%np.min(ScoreAll)+","+"%.2f"%np.median(ScoreAll)+","+"%.2f"%np.mean(ScoreAll)
    f.write(dt)
