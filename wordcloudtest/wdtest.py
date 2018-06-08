#coding:utf-8
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
import matplotlib.pyplot as plt
import jieba
import numpy as np
from PIL import Image

# 读入图片
able_mask = np.array(Image.open('bigdata.jpg'))
print(able_mask)

#读取要生成词云的文件
text_from_file_path = open('wordc.txt' , encoding="utf-8").read()

#通过jieba分词进行分词并通过换行分割
wordlist_after_jieba = jieba.cut(text_from_file_path, cut_all=True)
wl_split = r' '.join(wordlist_after_jieba)

#设置构造函数信息
my_wordcloud = WordCloud(
    background_color='white',   #设置背景颜色
    mask= able_mask,        #设置背景图片
    max_words= 2000,     #设置最大实现的字数
    stopwords= STOPWORDS,       #设置停用词
    font_path="C:/Users/Windows/fonts/simkai.ttf",           #设置字体格式
    max_font_size= 20,      #设置字体最大值
    random_state= 50,       #设置多少种随机生成状态，即多少种配色方案
    scale=.5
    ).generate(wl_split)

# 根据图片生成词云颜色
image_colors = ImageColorGenerator(able_mask)

# 显示出来图片
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
print(WordCloud.__doc__)
