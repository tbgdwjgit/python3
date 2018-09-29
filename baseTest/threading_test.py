__author__ = 'Test-YLL'

# coding:utf-8

# import threading
#
# def thrfun(x,y):
#     for i in range(x,y):
#         print(str(i*i)+';')
# ta = threading.Thread(target=thrfun,args=(1,6))
# tb = threading.Thread(target=thrfun,args=(16,21))
# ta.start()
# tb.start()

import  threading

class myThread(threading.Thread):
    def __init__(self,mynum):
        super().__init__()
        self.mynum = mynum

    def run(self):
        for i in range(self.mynum,self.mynum+5):
            print(str(i*i)+';')

ma = myThread(1)
mb = myThread(16)
ma.start()
mb.start()