#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/9/26 10:03'
__author__ = 'likunkun'

import threading

num = 0  #全局变量
lock = threading.Lock()  #生成全局锁
def add():
    global num  # 在每个线程中都获取这个全局变量
    lock.acquire()  # 修改数据前加锁
    num += 1  # 对此公共变量进行-1操作
    lock.release()  # 修改后释放

thread_list = []
for i in range(100):
    t = threading.Thread(target=add)
    t.start()
    thread_list.append(t)

for t in thread_list:  # 等待所有线程执行完毕
    t.join()

print('final num:', num)