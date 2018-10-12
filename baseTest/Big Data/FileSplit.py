__author__ = 'Test-YLL'

# coding:utf-8
'''
分割文件
'''

import os,os.path,time

def FileSplit(sourceFile,targetFolder):
    sFile = open(sourceFile,'r',errors='ignore')
    '''
   python读取中编码错误（illegal multibyte sequence ）
   读取中文txt文件时，经常会出现: ‘gbk' codec can't decode bytes in position 31023: illegal multibyte sequence。
   这种情况就是文章中含有utf-8或gbk无法编码的字符情况。
   好多人都说加入'ignore'，但一直都没有说清楚是在open函数中加入，还是在.read()中加入（其实是在open函数中加入，如下面例子）。
   'gb1830'所含的比'gbk'要多，因此下面代码段采用了'gb1830'。
   cf=open("D:\python_code\天龙八部.txt",encoding='gb18030',errors='ignore')
   cf1=cf.read()
   '''
    number = 50000 #每个文件保存记录条数
    dataLine = sFile.readline()
    tempData = [] #缓存列表
    fileNum = 1
    if not os.path.isdir(targetFolder):#目标目录不存在，则创建
        os.mkdir(targetFolder)

    while dataLine: #有数据
        for row in range(number):
            tempData.append(dataLine)#增加一行数据到列表
            dataLine = sFile.readline()
            if not dataLine: #没有数据需要保存
                break
        tfilename = os.path.join( targetFolder,os.path.split(sourceFile)[1] + str(fileNum) + ".txt")
        tfile = open(tfilename,'a+') #创建小文件
        tfile.writelines(tempData) #将临时列表保存到文件中
        tfile.close()
        tempData = [] #清空缓存列表
        print(tfilename +"创建于：" + str(time.ctime()))
        fileNum += 1 #文件编号

    sFile.close()

if __name__ == "__main__":
    FileSplit("SeekView.log","SeekView")