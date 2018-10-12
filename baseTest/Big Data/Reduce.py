__author__ = 'Test-YLL'

# coding:utf-8

import os,os.path,re

def Reduce(sourceFolder,targetFile):
    tempData = {}  #缓存列表
    p_re = re.compile(r'(.*?)(\d{1,}$)',re.IGNORECASE) #用正则表达式解析数据
    for root,dirs,files in os.walk(sourceFolder):
        for fil in files:
            if fil.endswith('_map.txt'):
                sFile = open(os.path.abspath(os.path.join(root,fil)),'r')
                dataLine = sFile.readline()

                while dataLine:
                    subdata = p_re.findall(dataLine) #用空格分割数据
                    #print(subdata[0][0]," ",subdata[0][1])
                    if subdata[0][0] in tempData:
                        tempData[subdata[0][0]] += int(subdata[0][1])
                    else:
                        tempData[subdata[0][0]] = int(subdata[0][1])
                    dataLine = sFile.readline()  #读取下一行数据

                sFile.close()

    tList =[]
    for key,value in sorted(tempData.items(),key = lambda k:k[1],reverse=True):
        tList.append(key + " " + str(value) + '\n')

    tFilename = os.path.join(sourceFolder,targetFile + "_reduce.txt")
    tFile = open(tFilename,'a+') #创建小文件
    tFile.writelines(tList)      #保存列表到文件
    tFile.close()

if __name__ == "__main__":
    Reduce("SeekView","SeekView")