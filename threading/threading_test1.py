#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/9/11 15:36'
__author__ = 'likunkun'

import threading
import time


#用方法来写
def run(n):
    print("run",n)
    time.sleep(2)

# t1 = threading.Thread(target=run,args=("1",))
# t2 = threading.Thread(target=run,args=("2",))
#
# t1.start()
# t2.start()

'''
#用类来写
class myThread(threading.Thread):
    def __init__(self, n):
        super(myThread, self).__init__()
        self.n = n
    def run(self):
        print("runing task", self.n)

t1 = myThread("1")
t2 = myThread("2")

t1.start()
t2.start()
'''


for i in range(50):
    t1 = threading.Thread(target=run, args=("1",))
    t2 = threading.Thread(target=run,args=("2",))

    t1.start()
    t2.start()
'''
#当运行多个线程的时候，如果要计时，主线程默认是不等别的线程的
#如果要让他等别的线程运行完再继续
要用t1.join()方法，等待t1运行完才继续主线
'''





