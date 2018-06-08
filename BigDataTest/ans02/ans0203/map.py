#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/24 10:06
# @Author  : BlackHawk
# @File    : map.py
# @Software: PyCharm Community Edition
import sys

for line in sys.stdin:
    line = line.strip()
    words = filter(lambda word: word, line.split(';'))
    for word in words:
        word = word.split('\t')[0]
        print '%s\t%s' % (word, 1)
