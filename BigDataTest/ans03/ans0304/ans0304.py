#coding=utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#数据预处理
names=['name','s_time','e_time','bor','city']
df = pd.read_csv('film_log3.csv',sep=';',names=names,usecols=[0,1,2,7,8])
df['s_time'] = pd.to_datetime(df['s_time'])
df['e_time'] = pd.to_datetime(df['e_time'])
df['bor'] = df['bor'].str.split(')').str[1].astype(float)
#各城市日平均票房
daily_mean=[]
for i in xrange(len(df)):
    date = (df['e_time'][i]-df['s_time'][i]).days+1
    bor = df['bor'][i]
    daily_mean.append(bor/date)

df['daily_mean'] = daily_mean
#选取16年 1-3月作为计算周期   1.1-4.1涵盖1-3月 不以1.1-3.31作为计算周期
s_date=  pd.to_datetime('2016.1.1')
e_date=  pd.to_datetime('2016.4.1')
period = (e_date-s_date).days#周期内的总天数
#选取城市 对时间进行初步筛选，剔除和去重
M =df[(df['city']=='上海')&(df['s_time']<=e_date)&(df['e_time']>=s_date)].drop_duplicates()
N =df[(df['city']=='北京')&(df['s_time']<=e_date)&(df['e_time']>=s_date)].drop_duplicates()


#计算各月票房
#从1.1-4.1日对日票房进行累加
#截取月份时间段 31 29 31
#返回月票房列表
def m_bor(n):
    bor_sum=[]
    for i in xrange(period):
        temp_date= s_date+pd.Timedelta(days=i)
        temp_bor =n[(n['s_time']<=temp_date)&(n['e_time']>=temp_date)]['daily_mean'].sum()
        bor_sum.append(temp_bor)
    bor_sum=np.nan_to_num(bor_sum)
    month_bor=[sum(bor_sum[0:31]),sum(bor_sum[31:60]),sum(bor_sum[60:len(bor_sum)])]

    return month_bor


M_mbor=m_bor(M)
N_mbor=m_bor(N)
with open('ans0304.dat','w') as f:
    f.write('%.6f,%.6f,%.6f\n'%(M_mbor[0],M_mbor[1],M_mbor[2]))
    f.write('%.6f,%.6f,%.6f'%(N_mbor[0],N_mbor[1],N_mbor[2]))
#绘制图表
plt.rcParams['font.family']='Fangsong'
fig = plt.figure()
ax1 = fig.add_subplot(121)
ax1.plot(range(1,4),M_mbor)
ax1.set_title(u'上海 2016 1-3 BOR')
ax1.set_xlabel(u'时间')
ax1.set_ylabel(u'票房收入(万元)')
ax1.set_xlim(0,3)
ax2 = fig.add_subplot(122)
ax2.plot(range(1,4),N_mbor)
ax2.set_title(u'北京 2016 1-3 BOR')
ax2.set_xlabel(u'时间')
ax2.set_ylabel(u'票房收入(万元)')
ax2.set_xlim(0,3)

plt.savefig('ans0304.jpg')
plt.show()