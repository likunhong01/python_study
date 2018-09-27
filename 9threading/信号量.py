#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/9/26 10:35'
__author__ = 'likunkun'

import threading, time
#信号量

def run(n):
    semaphore.acquire()
    time.sleep(1)   #控制每个线程1秒运行时间
    print("run the thread: %s\n" % n)
    semaphore.release()

semaphore = threading.BoundedSemaphore(3)  # 最多允许5个线程同时运行
for i in range(20):
    t = threading.Thread(target=run, args=(i,))
    t.start()

while threading.active_count() != 1:    #还有线程在活动就不结束
    pass
else:
    print('----all threads done---')

