# coding=UTF-8
import urllib2

url = "https://www.taobao.com/"
html = urllib2.urlopen(url)

read=html.read()

File = open("E:\\tb.html" ,"w")
File.write(read)


File.close()


str="""
    aaa
    bbb
    ccc
    """

str1="a" \
     "b" \
     "c" \

print str
print str1