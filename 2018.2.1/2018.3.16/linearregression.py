#coding=utf-8
import pandas as pd
import re
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

f=plt.figure()
ax1=f.add_subplot(311)
ax2=f.add_subplot(312)
ax3=f.add_subplot(313)
plt.rcParams["font.sans-serif"]="SimHei"

info=pd.read_csv("film-csv.txt",encoding="utf-8",sep=";")
content=info.ix[:,:-1]
content=content.dropna().drop_duplicates().reset_index().drop("index",axis=1)
#print content

t=[]
tt=[]
for i in range(len(content)):
    ls=re.split(u" / |、| |，|/",content[u"影片类型"][i])
    for k in ls:
        t.append(k)
t=list(set(t))
#print t

for i in t:
    if len(i)<=2:
        tt.append(i)
lst=[]
lsb=[]
for i in range(len(content)):
    for j in tt:
        if j in content[u"影片类型"][i]:
            lst.append(j)
            lsb.append(content[u"票房/万"][i])
lst=pd.DataFrame(lst,columns=[u"类型"])
lsb=pd.DataFrame(lsb,columns=[u"票房/万"])
lstb=pd.concat([lst,lsb],axis=1)
lstb=lstb.groupby(u"类型").sum().sort_values(u"票房/万")
lstb.plot(kind="bar", ax=ax1, title=u"类型-票房图")

lsd=[]
lsb=[]
for i in range(len(content)):
    ls=re.split(u"，|、|/",content[u"导演"][i])
    for j in ls:
        lsd.append(j)
        lsb.append(content[u"票房/万"][i])
lsd=pd.DataFrame(lsd,columns=[u"导演"])
lsb=pd.DataFrame(lsb,columns=[u"票房"])
lsdb=pd.concat([lsd,lsb],axis=1)
lsdb=lsdb.groupby(u"导演").sum().sort_values(u"票房")
lsdb.plot(kind="bar",ax=ax2,title=u"导演-票房图")

lsd=[]
lst=[]
for i in range(len(content)):
    for j in tt:
        if j in content[u"影片类型"][i]:
            ls=re.split(u"，|/|、",content[u"导演"][i])
            for d in ls:
                lst.append(j)
                lsd.append(d)
lsd1=list(set(lsd))
for i in range(len(lsd)):
    for j in range(len(lsd1)):
        if lsd[i]==lsd1[j]:
            lsd[i]=j+1
for i in range(len(lst)):
    for j in range(len(tt)):
        if lst[i]==tt[j]:
            lst[i]=j+1
lsd=pd.DataFrame(lsd,columns=[u"导演"])
lst=pd.DataFrame(lst,columns=[u"类型"])
lsdt=pd.concat([lsd,lst],axis=1)
for i in range(len(lsdt)):
    ax3.scatter(lsdt[u"导演"][i],lsdt[u"类型"][i])

id=[1050,1114,1048,1488,1102]
info2=pd.read_csv("score.log",sep=",",header=0,encoding="utf-8",names=[u"电影名称",u"userid",u"score"])
info2=info2[info2[u"userid"].isin(id)]
info2[u"电影名称"]=info2[u"电影名称"].str.strip()
all=[]
for k in range(len(id)):
    total=info2[info2[u"userid"]==id[k]].reset_index().drop("index",axis=1)
    quanbu=pd.merge(total,content,on=u"电影名称")
    lsd=[]
    lst=[]
    lsr=[]
    for i in range(len(quanbu)):
        for j in tt:
            if j in quanbu[u"影片类型"][i]:
                ls=re.split(u"，|/|、",quanbu[u"导演"][i])
                for k in ls:
                    lsd.append(k)
                    lst.append(j)
                    lsr.append(quanbu[u"score"][i])
    lsd1=list(set(lsd))
    for i in range(len(lsd)):
        for j in range(len(lsd1)):
            if lsd[i]==lsd1[j]:
                lsd[i]=j+1
    for i in range(len(lst)):
        for j in range(len(tt)):
            if lst[i]==tt[j]:
                lst[i]=j+1
    lsd=pd.DataFrame(lsd,columns=[u"导演"])
    lst=pd.DataFrame(lst,columns=[u"类型"])
    lsr=pd.DataFrame(lsr,columns=[u"评分"])
    sanxiang=pd.concat([lsd,lst,lsr],axis=1)
    lianxix=sanxiang.ix[:,0:2]
    lianxiy=sanxiang.ix[:,2:3]
    l=LinearRegression()
    l.fit(lianxix,lianxiy)

    ans=pd.DataFrame([[5,10]],columns=[u"导演",u"类型"])
    end=l.predict(ans)
    all.append(end[0][0])
print max(all)
print min(all)
print np.mean(all)
print np.median(all)