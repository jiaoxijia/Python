# --*-- coding="UTF-8" --*--
# import copy
# a =[11,22,333]
#
# #b = [11,22,33]
# #c=[a,b]
# #print(id(a))
# b = copy.deepcopy(a)
# #print(id(b))
# #a,b = b,a+b
# #print(b)
#
#
# #定义函数：完成包裹数据
# def makeBold(fn):
#     def wrapped():
#         return "<b>" + fn() + "</b>"
#     return wrapped
#
# #定义函数：完成包裹数据
# def makeItalic(fn):
#     def wrapped():
#         return "<i>" + fn() + "</i>"
#     return wrapped
#
# @makeBold
# def test1():
#     return "hello world-1"
#
# @makeItalic
# def test2():
#     return "hello world-2"
#
# @makeBold
# @makeItalic
# def test3():
#     return "hello world-3"
#
# print(test1())
# print(test2())
# print(test3())

def line_conf(a, b):
    def line(x):
        return a*x + b
    return line

line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
print(line1(5))
print(line2(5))

#定义函数：完成包裹数据
def makeBold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

#定义函数：完成包裹数据
def makeItalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makeBold
def test1():
    return "hello world-1"

@makeItalic
def test2():
    return "hello world-2"

@makeBold
@makeItalic
def test3():
    return "hello world-3"

print(test1())
print(test2())
print(test3())

