# -*- coding: UTF-8 -*-

#可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(3,4))

#命名关键字参数
def person(name,age,*,city,job):
    print(name,age,city,job)

person('zll',"lala",city="成都",job='teacher')
# person('zll','18',)

#匿名函数
func=lambda x:x+1

#普通函数
# def func(x):
#     a = x+1
#     return a

print(func(11))

#列表脚本操作
print([1,2,3]+[4,5,6]*3)

#列表切割
a = [1,2,3,4,5]
print(a[0:6:2])

#定义一个元组
b = (a,1,3)
print(b)
b[0][4] = 8
print(b)

a = list(b)
print(a)
c = tuple(a)
print(c)

d = {"a":1,
     "b":2,
     "c":3}
print(d)

d['a'] = 0
print(d)

print(d.pop('a'))

# del d['b']
# print(d)
#
# print(d.clear())

print(len(d))
print(type(str(d)))
print(d.keys())
print(d.values())
print(d.items())
print("d" in d)
