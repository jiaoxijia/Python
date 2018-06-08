import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1,2,3,5,np,'nan',6,8])
print type(s)

dates = pd.date_range('2013-01-03',periods=6)
print dates

df = pd.DataFrame(np.random.rand(6,4), index=dates, columns=list('ABCD'))
print df

df2 = pd.DataFrame({'A':1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D': np.array([3]*4,dtype='int32'),
                    'E': pd.Categorical(["test","train","test","train"]),
                    'F':'foo'})
print df2
print df2.dtypes

print df.head()
print df.tail(3)
print df.index

print df.columns
print df.values
print df.describe()
print df.T

print df.sort_index(axis=1, ascending=False)

print df.sort_values(by='B')
