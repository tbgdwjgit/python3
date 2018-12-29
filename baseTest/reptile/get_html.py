__author__ = 'Test-YLL'

# coding:gbk

import urllib.request
import re
import time

def getContent(url,page,txtF):
    #模拟浏览器
    headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3251.400 QQBrowser/9.5.10937.400')
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    #将opener安装为全局
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode("gbk")
    #print(type(data))
    #print(data)


    #构建段子内容提取的正则表达式
    contentpat='<div class="novelcontent">(.*?)</div>'
    #寻找出所有的内容
    contentlist = re.compile(contentpat,re.S).findall(data)

    if contentlist:#由于一个空 list 本身等同于 False，所以可以直接：
        txtF.write(str(contentlist[0]))
        txtF.write('==================page'+ str(page) +'==================')


#分别获取各页的段子，通过for循环可以获取多页
#fhandle = open('1.txt','a')
#url='http://www.baidu.com/5444310.html'
#getContent(url,0,fhandle)

#for i in range(1,25):
    #url='http://www.baidu.com/read/'+str(5444310+i)  +'.html'
    #print(url)
    #getContent(url,i,fhandle)
    ##if i // 10 > 0:
        ##time.sleep(5)
        ##print(i)
    ##else:
    #time.sleep(5)
#fhandle.close()


'''  htmlToPdf    '''

# coding=utf-8
import os
import re
import time
import logging
import pdfkit
import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfFileMerger
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>
<body>
{content}
</body>
</html>
"""
def parse_url_to_html(url, name):
    """
    解析URL，返回HTML内容
    :param url:解析的url
    :param name: 保存的html文件名
    :return: html
    """
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # 正文
        body = soup.find_all(class_="x-wiki-content")[0]
        # 标题
        title = soup.find('h4').get_text()
        # 标题加入到正文的最前面，居中显示
        center_tag = soup.new_tag("center")
        title_tag = soup.new_tag('h1')
        title_tag.string = title
        center_tag.insert(1, title_tag)
        body.insert(1, center_tag)
        html = str(body)
        # body中的img标签的src相对路径的改成绝对路径
        pattern = "(<img .*?src=\")(.*?)(\")"
        def func(m):
            if not m.group(3).startswith("http"):
                rtn = m.group(1) + "http://www.liaoxuefeng.com" + m.group(2) + m.group(3)
                return rtn
            else:
                return m.group(1)+m.group(2)+m.group(3)
        html = re.compile(pattern).sub(func, html)
        html = html_template.format(content=html)
        html = html.encode("utf-8")
        with open(name, 'wb') as f:
            f.write(html)
        return name
    except Exception as e:
        logging.error("解析错误", exc_info=True)
def get_url_list():
    """
    获取所有URL目录列表
    :return:
    """
    response = requests.get("http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000")
    soup = BeautifulSoup(response.content, "html.parser")
    menu_tag = soup.find_all(class_="uk-nav uk-nav-side")[1]
    urls = []
    for li in menu_tag.find_all("li"):
        url = "http://www.liaoxuefeng.com" + li.a.get('href')
        urls.append(url)
    return urls
def save_pdf(htmls, file_name):
    """
    把所有html文件保存到pdf文件
    :param htmls: html文件列表
    :param file_name: pdf文件名
    :return:
    """
    options = {
      'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'custom-header': [
        ('Accept-Encoding', 'gzip')
      ],
    'cookie': [
        ('cookie-name1', 'cookie-value1'),
      ('cookie-name2', 'cookie-value2'),
      ],
    'outline-depth': 10,
  }
    pdfkit.from_file(htmls, file_name, options=options)
def main():
    start = time.time()
    file_name = u"liaoxuefeng_Python3_tutorial"
    urls = get_url_list()
    for index, url in enumerate(urls):
        parse_url_to_html(url, str(index) + ".html")
    htmls =[]
    pdfs =[]
    for i in range(0,124):
        htmls.append(str(i)+'.html')
        pdfs.append(file_name+str(i)+'.pdf')
        save_pdf(str(i)+'.html', file_name+str(i)+'.pdf')
        print (u"转换完成第"+str(i)+'个html')
    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(open(pdf,'rb'))
        print (u"合并完成第"+str(i)+'个pdf'+pdf)
    output = open(u"廖雪峰Python_all.pdf", "wb")
    merger.write(output)
    print (u"输出PDF成功！")
    for html in htmls:
        os.remove(html)
        print (u"删除临时文件"+html)
    for pdf in pdfs:
        os.remove(pdf)
        print (u"删除临时文件"+pdf)
    total_time = time.time() - start
    print(u"总共耗时：%f 秒" % total_time)
if __name__ == '__main__':
    main()
