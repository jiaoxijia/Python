# -*- coding:UTF-8 -*-
import time

ticks = time.time()

print '当前时间戳为：',ticks

#获取当前本地时间

# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# 格式化成Sat Mar 28 22:24:24 2016形式
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import calendar

cal = calendar.month(2018, 1)
print "以下输出2018年1月份的日历:"
print cal;

import datetime
i = datetime.datetime.now()

print "当前日期和时间是 %s"  %i
print "ISO格式的日期和时间是 %s" %i.isoformat()
print "当前年份的时间是 %s" %i.year
print "当前月份的时间是 %s" %i.month
print "当前日期是 %s" %i.day
