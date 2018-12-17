__author__ = 'Test-YLL'

# coding utf-8
'''
百度搜索
'''
from urllib.request import urlopen
from urllib.parse import urlencode
import re

wd = input(' 输入一个要搜索的关键字：')
#wd = 'python'
wd = urlencode({'wd':wd})
url = 'http://www.baidu.com/s?' + wd
page = urlopen(url).read()
content = (page.decode('utf-8')).replace("\n","").replace("\t","")
title = re.findall(r'<h3 class="t".*?h3>',content)
title = [item[item.find('href=')+6:item.find('target=')] for item in title]
title = [item.replace(' ','').replace('"','') for item in title]
for item in title:
    print(item)


'''
HTTPConnection
'''
from http.client import HTTPConnection

mc = HTTPConnection('www.baidu.com:80')
mc.request('GET','/')
res = mc.getresponse()
print(res.status,res.reason)
print(res.read().decode('utf-8'))


"""
import urllib.request

#file = urllib.request.urlopen('http://www.baidu.com')
##data = file.readlines()
#data1 = file.read()
##for d in data:
    ##print(d)
#fhandle = open('1.html','wb')
#fhandle.write(data1)
#fhandle.close()


'''
#urllib.request.urlretrieve('http://www.baidu.com',filename='2.html')
#urllib.request.urlretrieve('http://edu.51cto.com',filename='2.html')
urllib.request.urlretrieve('http://www.163.com',filename='2.html')
urllib.request.urlcleanup
'''

'''build_opener()'''
##url = 'http://blog.csdn.net/weiwei_pig/article/details/51178226'
#url = 'http://www.baidu.com'
#headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3251.400 QQBrowser/9.5.10937.400')
#opener = urllib.request.build_opener()
#opener.addheaders = [headers]
#data = opener.open(url).read()

#fhandle = open('11.html','wb')
#fhandle.write(data)
#fhandle.close()

'''add_header()'''
url = 'http://www.baidu.com'
req = urllib.request.Request(url)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3251.400 QQBrowser/9.5.10937.400')
data =urllib.request.urlopen(req).read()
fhandle = open('111.html','wb')
fhandle.write(data)
fhandle.close()


# for i in range(1,10):
#     try:
#         file = urllib.request.urlopen('http://www.baidu.com',timeout=1)
#         data = file.read()
#         print(len(data))
#     except Exception as e:
#         print('出现异常-->'+ str(e))

keywd='hello'
url='http://www.baidu.com/s?wd='+keywd
'''
  中文要编码
'''
keywd='长城号'
key_code=urllib.request.quote(keywd)


url='http://www.baidu.com/s?wd='+key_code
req=urllib.request.Request(url)
data=urllib.request.urlopen(req).read()
fhandle=open('E:/test1217.html','wb')
fhandle.write(data)
fhandle.close()

"""