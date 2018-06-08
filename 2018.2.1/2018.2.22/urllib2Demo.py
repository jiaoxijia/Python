import urllib.request
response = urllib.request.urlopen('http://www.baidu.com')
result = response.read()
print(result)