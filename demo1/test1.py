s1 = {"1001":'旺财','1002':'小强','1003':'阿黄'}
s2 = s1.copy()
print(s1,s2,id(s1),id(s2))
s3 = s1.fromkeys(['1','3'],'哈哈')
print(s3)

s3.setdefault('1111','22')
print(s3)
# s1.setdefault()