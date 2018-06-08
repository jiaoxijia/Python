# --*-- coding:UTF-8 --*--
import re
# import os
# # rd = os.rmdir()
#
# result = re.match("[\u4e00-\u9fa5]",'啦啦啦123aannbbaa12313,DDaa')
#
# #result.string
# print(result.group())
# ret = re.match("[a-zA-Z0-9_]{6}","12a3g45678")
# ret.group()
#
# ret = re.match("[a-zA-Z0-9_]{8,20}","1ad12f23s34455ff66")
# ret.group()
#
#
# # ret00 = re.match(r'\d',"123abcABC")
# # print(ret00.group())
# ret = re.match("[a-zA-Z0-9_]{8,20}","fdsfdsfdsfs1ad12f23s34455ff66")
#
# print(ret.group())

# #错误的匹配规则
# ret = re.match("[\w]{4,20}@163\.com", "xiaoWang@163.comheihei")
# print(ret.group())
#
# # 通过$来确定末尾
# ret = re.match("[\w]{4,20}@163\.com$", "xiaoWang@163.com")
# print(ret.group())

# # 不正确的情况
# ret = re.match("[1-9]?\d$","08")
# print(ret.group())

# 修正之后的
# ret = re.match("[0-9]?\d$","08")
# print(ret.group())
#
# ret = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")
# print(ret)

#re的用法
#尝试在字符串的开头应用模式，返回一个匹配对象，如果没有找到匹配项，则为None
#ret = re.match()


"""返回字符串中所有不重叠匹配的列表。

     如果模式中存在一个或多个捕获组，则返回
     小组名单; 这将是一个元组的列表，如果模式
     有不止一个组。

     空结果包含在结果中。"""
#ret1 = re.findall()

"""扫描字符串寻找匹配的模式，返回
     一个匹配对象，如果没有找到匹配项，则为None。"""
#ret2 = re.search()
#ret3 = re.sub() #对匹配到的内容进行替换

# #根据匹配进行切割
# ret = re.split(r":| ","info:xiaoZhang 33          shandong")
#
# print(ret)
# print(type(ret))



