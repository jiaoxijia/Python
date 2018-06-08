# -*- coding:utf-8 -*-
import numpy as np
'''1.用列表, 元组等创建.'''
# print np.array([1, 2, 3, 4])

a = np.array([[1,2], [3,4], (0.5,0.6)]) # 支持列表, 元组混合
print a
'''2.用numpy中的函数创建.'''
np.arange(10) # 类似range, 但返回ndarray类型
b = np.ones((3, 6), dtype=np.int32) # 根据shape生成全为1的数组, 这里指定了数据类型
print b
np.zeros(3) # 根据shape生成全为0的数组
np.full((3,3,3), 10) # 根据shape生成全为10的数组
np.eye(5) # 创建一个5*5的单位矩阵, 对角线为1, 其余为0
np.linspace(1, 10, 4) # 1到10之间(包括10), 均匀选取4个数据
np.linspace(1, 10, 4, endpoint=False) # 此时不包括10
# c = np.concatenate((a, b)) # 合并a, b两个数组, 返回一个新数组
# print c
# np.ones_like(x) # 生成和x相同shape的全1数组
# np.zeros_like(x) # 生成和x相同shape的全0数组
# np.full_like(x, 3) # 生成和x相同shape的全3数组