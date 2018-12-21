__author__ = 'Test-YLL'

# coding:utf-8
'''链接爬虫'''
import  re
import urllib.request
def getlink(url):
    #模拟成浏览器
    headers =('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3251.400 QQBrowser/9.5.10937.400')
    opener = urllib.request.build_opener()
    opener.addheaders =[headers]
    #将opener安装为全局
    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url)
    data = str(file.read())
    #根据需求构建好链接表达式
    pat = '(https?://[^\s]+\.(\w|/)*)'
    link = re.compile(pat).findall(data)
    #去除重复元素
    link = list(set(link))
    return link

#要爬取的网页链接
url ='http://blog.csdn.net/'
url ='https://www.baidu.com/?tn=98010089_dg&ch=8'
url ='http://www.ifeng.com/?from=newtab'
url ='http://www.163.com/?from=newtab'
#获取对应网页中包含的链接地址
linklist = getlink(url)
#通过for循环分别遍历输出获取到的链接地址到屏幕上
for link in linklist:
    print(link[0])

