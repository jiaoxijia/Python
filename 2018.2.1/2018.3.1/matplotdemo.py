from datetime import datetime
import numpy as np
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

# 生成横纵坐标信息
dates = ['01/02/1991', '01/15/1991','01/30/1991']
xs = [datetime.strptime(d, '%m/%d/%Y').date() for d in dates]
ys = range(len(xs))
# 配置横坐标
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

# Plot
aaa = np.arange(3)
plt.plot(aaa, ys)
plt.xticks(aaa,("aa","bb","cc"))
plt.gcf().autofmt_xdate()  # 自动旋转日期标记
plt.show()