#coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
'''
大致思路：
    求出各影片的上映总天数，求出每个城市的日平均票房，再计算该影片从最早放映时间到最晚放映时间
    日票房累加的和，按照周数进行截取求和，计算出该影片的周票房
'''
names=['name','s_time','e_time','bor','city']
df = pd.read_csv('film_log3.csv',sep=';',names=names,usecols=[0,1,2,7,8])
df['s_time'] = pd.to_datetime(df['s_time'])
df['e_time'] = pd.to_datetime(df['e_time'])
df['bor'] = df['bor'].str.split(')').str[1].astype(float)
#求出各城市的日平均票房
daily_mean=[]
for i in xrange(len(df)):
    date = (df['e_time'][i]-df['s_time'][i]).days+1
    bor= df['bor'][i]
    daily_mean.append(bor/date)
#将计算完成的日平均加入 DataFrame
df['daily_mean'] = daily_mean
#上映天数 和 周数
period = lambda x:(x['e_time'].max()-x['s_time'].min()).days+1
week = lambda y:y//7+(y%7>0)
A = df[df['name']=='《少年班》'].drop_duplicates()
B = df[df['name']=='《紫霞》'].drop_duplicates()
C = df[df['name']=='《浪漫天降》'].drop_duplicates()
#计算各影片的上映天数
A_period = period(A)
B_period = period(B)
C_period = period(C)
#上映周数
A_week = week(A_period)
B_week = week(B_period)
C_week = week(C_period)
#计算周票房的方法
#从最早放映到最晚放映时间进行累加
#并进行周数的切割
#返回周票房列表
def w_bor(p,n):
    bor_sum=[]
    for i in xrange(p):
        temp_date=n['s_time'].min()+pd.Timedelta(days=i)
        temp_bor = n[(n['s_time']<=temp_date)&(n['e_time']>=temp_date)]['daily_mean'].sum()
        bor_sum.append(temp_bor)
    week_bor=[]
    for j in xrange(0,len(bor_sum),7):
        week_bor.append(sum(bor_sum[j:j+7]))
    return week_bor

A_wbor = w_bor(A_period,A)
B_wbor = w_bor(B_period,B)
C_wbor = w_bor(C_period,C)
#将A的第一周 B的第二周 C的第三周票房依次写入文件
with open('ans0303.dat','w') as f:
    f.write('%.6f,%.6f,%.6f'%(A_wbor[0],B_wbor[1],C_wbor[2]))
#进行周票房趋势图的绘制
plt.rcParams['font.family']='Fangsong'
fig = plt.figure()
ax =fig.add_subplot(111)
ax.plot(range(1,A_week+1),A_wbor,'g-',label=u'少年班')
ax.plot(range(1,B_week+1),B_wbor,'r--',label=u'紫霞')
ax.plot(range(1,C_week+1),C_wbor,'c:',label=u'浪漫天降')
ax.set_ylabel(u'票房收入(万元)')
ax.set_xlabel(u'时间(周)')
ax.set_xlim(0,7)
ax.legend()
plt.savefig('ans0303.jpg')
plt.show()