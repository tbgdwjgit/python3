__author__ = 'Test-YLL'

# coding:utf-8
'''
分割文件
'''

import os,os.path,time

def FileSplit(sourceFile,targetFolder):
    sFile = open(sourceFile,'r')
    number = 500 #每个文件保存记录条数
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