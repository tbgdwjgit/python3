__author__ = 'Test-YLL'

# coding:utf-8


'''
reptile
英[ˈreptaɪl]
美[ˈrɛptɪl, -ˌtaɪl]
n.	爬行动物; 卑鄙的人;
adj.爬虫类的; 卑鄙的;
[例句]Is not a reptile but a mammal.
     并不是爬虫动物，而是哺乳动物。
'''

import re
import urllib.request


'''京东手机图 '''
'''
def craw(url,page):
    html1=urllib.request.urlopen(url).read()
    html1=str(html1)
    pat1='<div id="plist".+?<div class="page clearfix">'
    result1=re.compile(pat1).findall(html1)
    result1=result1[0]
    # pat2='<img width="220" height="220" data-img="1"data-lazy-img="//(.+?\.jpg)">'
    pat2='<img width="220" height="220" data-img="1" src="//(.+?\.jpg)">'
    imagelist=re.compile(pat2).findall(result1)
    x=1
    for imageurl in imagelist:
        imagename='e:/test1221/'+str(page) + str(x) + ".jpg"
        imageurl="http://"+imageurl
        try:
            urllib.request.urlretrieve(imageurl,filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                x+=1
            if hasattr(e,"reason"):
                x+=1
        x+=1

for i in range(1,7):
    url = "http://list.jd.com/list.html?cat=9987,653,655&page="+str(i)
    craw(url,i)
'''




''' test '''



