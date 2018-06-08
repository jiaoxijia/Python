#! --*-- coding:utf-8 --*--
import pandas as pd

import os

df = pd.read_csv("spider.log",delimiter=',',names=['date','www','film','piao','aa'])

print df.columns
df.dropna()
# print df.columns
df['www'] == r"http://www.movie.com/dor/"

# print df


# print df
