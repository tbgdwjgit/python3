__author__ = 'Test-YLL'
# coding:utf-8
# import os
import time
import urllib.request
import requests
from bs4 import BeautifulSoup
import pdfkit

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

def get_url_list():
    """
    获取所有URL目录列表
    :return:
    """
    # response = requests.get("http://www.187ks.cc/read/18356/5394310.html")
    # soup = BeautifulSoup(response.content, "html.parser")
    # print(soup)
    # menu_tag = soup.find_all(class_="novelcontent")[0]
    # # print(menu_tag)
    # urls = []
    # for li in menu_tag.find_all("li"):
    #     url = "http://www.liaoxuefeng.com" + li.a.get('href')
    #     urls.append(url)

    urls = []
    for i in range(0,108):
        response = requests.get("http://www.baidu.com/"+ str(5394310 + i) +".html")
        soup = BeautifulSoup(response.content, "html.parser")
        # print(soup)
        contentList =soup.find_all(class_="novelcontent")
        if contentList:
            menu_tag = contentList[0]
            # print(menu_tag)#获取内容

            html = html_template.format(content=menu_tag)#保存Html
            html = html.encode("utf-8")
            with open('E://1.html','ab') as f:
                f.write(html)


        time.sleep(8)

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

    # path_wk = r"C:\Users\Test-YLL\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\wkhtmltopdf\main.py" #安装位置
    # config = pdfkit.configuration(wkhtmltopdf = path_wk)
    pdfkit.from_file(htmls, file_name, options=options)


'''主方法'''
def main():
    start = time.time()

    file_name = u"liaoxuefeng_Python3_tutorial"
    urls = get_url_list()
    # save_pdf(['E:/1.html'],'test.pdf')??
    # for index, url in enumerate(urls):
    #     parse_url_to_html(url, str(index) + ".html")
    # htmls =[]
    # pdfs =[]
    # for i in range(0,124):
    #     htmls.append(str(i)+'.html')
    #     pdfs.append(file_name+str(i)+'.pdf')
    #     save_pdf(str(i)+'.html', file_name+str(i)+'.pdf')
    #     print (u"转换完成第"+str(i)+'个html')
    # merger = PdfFileMerger()
    # for pdf in pdfs:
    #     merger.append(open(pdf,'rb'))
    #     print (u"合并完成第"+str(i)+'个pdf'+pdf)
    # output = open(u"廖雪峰Python_all.pdf", "wb")
    # merger.write(output)
    # print (u"输出PDF成功！")
    # for html in htmls:
    #     os.remove(html)
    #     print (u"删除临时文件"+html)
    # for pdf in pdfs:
    #     os.remove(pdf)
    #     print (u"删除临时文件"+pdf)


    total_time = time.time() - start
    print(u"总共耗时：%f 秒" % total_time)

if __name__ == '__main__':
    main()
