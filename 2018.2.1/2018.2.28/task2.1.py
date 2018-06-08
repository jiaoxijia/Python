#--*-- coding:UTF-8 --*--
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

print(os.getcwd())

spiderlog = pd.read_csv(r"C:\FilmData\arg\arg\task0201\spider.log")
#print(spiderlog)
#print(spiderlog.get_dtype_counts())
#print(spiderlog._get_numeric_data())

print(spiderlog.head(5))
sl = spiderlog.head(10)

df = pd.DataFrame(sl)
ans0202 = df.to_csv("ans0202.txt")

print(ans0202)

# url = "www.douban.com"
# print(url)