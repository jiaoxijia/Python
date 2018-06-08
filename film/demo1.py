#coding=utf-8
import urllib
import urllib2

response = urllib2.urlopen("https://www.tmall.com/?pid=mm_26632258_3504122_48284354&b=ogfNNQOsM7QPMJ9sZ6g&ali_trackid=2:mm_26632258_3504122_48284354:1513562424_202_37744233&clk1=0089feea50e4bec9b9627dd490c90b26&upsid=0089feea50e4bec9b9627dd490c90b26")
print response.read()


# def getHtml(url):
#     page = urllib.urlopen(url)
#     html = page.read()
#     return html
#
# html = getHtml("https://www.baidu.com")
#
# print html

