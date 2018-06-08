#coding=utf-8
import pandas as pd
names = ['name','s_time','e_time','bor','city']
#数据读取 预处理 将需要的日期类型 和 票房进行转换
df = pd.read_csv('film_log3.csv',sep=';',names=names,usecols=[0,1,2,7,8])
df['s_time'] = pd.to_datetime(df['s_time'])
df['e_time'] = pd.to_datetime(df['e_time'])
df['bor'] = df['bor'].str.split(')').str[1].astype(float)
#计算电影上映周期
period = lambda x:(x['e_time'].max()-x['s_time'].min()).days+1
#选取电影
A = df[df['name']=='《少年班》'].drop_duplicates()
#计算A影片的上映时间
A_period = period(A)
#计算A的总票房
A_tbor = A['bor'].sum()
#计算日平均票房
A_daily_mean = A_tbor/A_period

with open('ans0301.dat','w') as f:
    f.write('%ld,%.6f'%(A_period,A_daily_mean))
# with 语句，不管在处理文件过程中是否发生异常，都能保证 with 语句执行完毕后已经关闭了打开的文件句柄