#coding:utf-8
import numpy as np
import pandas as pd
import matplotlib as plt  #65ans：matplotlib.pyplot

import string
dfxy=pd.read_csv('xyfilm.csv',delimiter=';',names=['fn','date','bor'],)
dfxypt=dfxy[['date','bor']]
dfpxy=dfxypt.sort_values(by='date', ascending=1) #66ans： 'date'#67ans：ascending=1
dfpxy['bor']=dfpxy['bor'] /10.0 #69ans：['bor']  #69ans：/10.0
dfpxy.index=dfpxy['date']
del dfpxy['date']
plt. title("BOR")  #70ans：title
plt.xlabel('day')
plt.ylabel('Box Office Return') #71ans：Box Office Return
dfpxy['bor'].plot(style='rD--') #72ans：rD--
plt.show()
