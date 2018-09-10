__author__ = 'Test-YLL'

# coding:utf-8

'''
一般而言，基础爬虫的两大请求库urllib和requests中requests通常为大多数人所钟爱，当然urllib也功能齐全。
两大解析库BeautifulSoup因其强大的HTML文档解析功能而备受青睐，另一款解析库lxml在搭配xpath表达式的基础上也效率提高。

pip install requests
pip install bs4
pip install lxml
'''

#requests+BeautifulSoup+select css选择器
'''import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
url = 'http://news.qq.com/'

Soup = BeautifulSoup(requests.get(url=url, headers=headers).text.encode("utf-8"), 'lxml')
em = Soup.select('em[class="f14 l24"] a')
for i in em:
    title = i.get_text()
    link = i['href']
    print({'标题': title, '链接': link})
'''
#requests+BeautifulSoup+find_all进行信息提取
'''import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
url = 'http://news.qq.com/'

Soup = BeautifulSoup(requests.get(url=url, headers=headers).text.encode("utf-8"), 'lxml')
em = Soup.find_all('em', attrs={'class': 'f14 l24'})
for i in em:
    title = i.a.get_text()
    link = i.a['href']
    print({'标题': title,
           '链接': link
    })
'''

#requests+lxml/etree+xpath表达式
'''import requests
from lxml import etree

headers = {    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
url = 'http://news.qq.com/'

html = requests.get(url = url, headers = headers)
con = etree.HTML(html.text)

title = con.xpath('//em[@class="f14 l24"]/a/text()')
link = con.xpath('//em[@class="f14 l24"]/a/@href')
for i in zip(title, link):
    print({'标题': i[0],
           '链接': i[1]
    })
'''

#requests+lxml/html/fromstring+xpath表达式
'''import requests
import lxml.html as HTML

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
url = 'http://news.qq.com/'

con = HTML.fromstring(requests.get(url = url, headers = headers).text)
title = con.xpath('//em[@class="f14 l24"]/a/text()')
link = con.xpath('//em[@class="f14 l24"]/a/@href')
for i in zip(title, link):
    print({'标题': i[0],'链接': i[1]
    #if i[0].find('油') > 0:
        #print({'标题': i[0],'链接': i[1]
    })
'''


import requests
from bs4 import BeautifulSoup
import webbrowser
import time
import string

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
url = 'http://news.qq.com/'

Soup = BeautifulSoup(requests.get(url=url, headers=headers).text.encode("utf-8"), 'lxml')
em = Soup.select('em[class="f14 l24"] a')


for i in em:
    title = i.get_text()
    link = i['href']
    #time.sleep(100)

    #if '武林怪兽' in title:
    '''
    检测字符串内是否包含子串str
    语法为：
    str.find(str[,start,end]) #str为要查找的字符串；strat为查找起始位置，默认为0；
    end为查找终止位置，默认为字符串长度。若找到返回起始位置索引，否则返回-1
    '''
    if title.find('中国') != -1 :
        webbrowser.open(link)#打开网页
        print({'标题': title, '链接': link})

#print(em)





