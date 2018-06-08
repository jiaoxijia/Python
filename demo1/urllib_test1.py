# # -*- coding:UTF-8 -*-
# from urllib import request
#
# #抓取首页 调用get_tie（）函数获取帖子个数
#     def get_Html_Data(self, url):
#         Ex_value = 1.7
#         userAgent = headerfile.USER_AGENTS
#         time.sleep(random.uniform(0.5, 1.6))
#         if url not in self.closetable:
#             request = urllib2.Request(url)
#             request.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
#             request.add_header('User-Agent', random.choice(userAgent))
#             proxy_handler = urllib2.ProxyHandler(random.choice(self.readIp()))
#             urllib2.build_opener(proxy_handler)
#             response = urllib2.urlopen(request,timeout=5)
#             if response.geturl() == url:
#                 htmlpage = response.read()
#                 self.get_tie(htmlpage)
#                 return htmlpage
#             else:
#                 return 0
#                 print '获取网页出错'
#         else:
#             print '已获取过该网页'
#
