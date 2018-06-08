#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/24 10:31
# @Author  : BlackHawk
# @File    : red.py
# @Software: PyCharm Community Edition
import sys

wc_dict = {}
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = int(count)
        wc_dict[word] = wc_dict.get(word, 0) + count
    except ValueError:
        pass

find = '《一个人的武林》'
for word, count in wc_dict.items():
    if (word == find):
        print '%s\t%s' % (word, count)
