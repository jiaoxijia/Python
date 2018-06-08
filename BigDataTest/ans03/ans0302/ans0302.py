#coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
#赛题中按照我个人理解不明白涉及列计算的地方在哪
names=['name','s_time','e_time','bor','city']
#数据预处理
df = pd.read_csv('film_log3.csv',sep=';',names=names,usecols=[0,1,2,7,8])
df['s_time'] = pd.to_datetime(df['s_time'])
df['e_time'] = pd.to_datetime(df['e_time'])
df['bor'] = df['bor'].str.split(')').str[1].astype(float)
#计算上映总日期和上映的周数
period = lambda x:(x['e_time'].max()-x['s_time'].min()).days+1
week = lambda y:y//7+(y%7>0)
#选取三部电影
A = df[df['name']=='《少年班》'].drop_duplicates()
B = df[df['name']=='《紫霞》'].drop_duplicates()
C = df[df['name']=='《浪漫天降》'].drop_duplicates()
#各自的上映的总天数
A_period = period(A)
B_period = period(B)
C_period = period(C)
#各自的上映的总周数
A_week = week(A_period)
B_week = week(B_period)
C_week = week(C_period)
#各自的总票房
A_tbor = A['bor'].sum()
B_tbor = B['bor'].sum()
C_tbor = C['bor'].sum()
#各自的周平均票房
A_week_avg= A_tbor/A_week
B_week_avg= B_tbor/B_week
C_week_avg= C_tbor/C_week
#对总票房进行排序 并写入文件
dat = sorted([A_tbor,B_tbor,C_tbor],reverse=True)
with open('ans0302.dat','w') as f:
    f.write('%.6f,%.6f,%.6f'%(dat[0],dat[1],dat[2]))


#对绘制图形的参数进行列表的整合
film_name=[u'少年班',u'紫霞',u'浪漫天降']
week_avg = [A_week_avg,B_week_avg,C_week_avg]

plt.rcParams['font.family']='Fangsong'
fig = plt.figure()
ax = fig.add_subplot(111)
#该方法绘制传参只能传入一个label参数  利用多个bar参数绘制可以有不同颜色的图例，matplotlib的版本问题
ax.bar(range(3),week_avg,0.3,alpha=0.6,tick_label=film_name,label=u'票房')
ax.legend()
ax.set_xlabel(u'电影名称')
ax.set_ylabel(u'票房收入(万元)')
plt.savefig('ans0302.jpg')
plt.show()
