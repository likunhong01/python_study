#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/9/18 12:46'
__author__ = 'likunkun'
'''
就是一堆事先创建好的进程。
进程池内部维护一个进程序列，当使用时，则去进程池中获取一个进程，
如果进程池序列中没有可供使用的进进程，那么程序就会等待，直到进程池中有可用进程为止。
'''
from multiprocessing import Process, Pool
import time,os

def Foo(i):
    time.sleep(1)
    return i + 100

def Bar(arg):
    print('-->exec done:', arg)

if __name__ == '__main__':
    pool = Pool(5)

    for i in range(10):
        pool.apply_async(func=Foo, args=(i,), callback=Bar)  # callback回调，执行完Foo再执行Bar
        # 用于执行完一些事情自动再干什么，比如批量备份，备份完自动往数据库写一条日志

        #pool.apply_async(func=Foo, args=(i,))  #并行
        pool.apply(func=Foo, args=(i,))  # 串行

    print('end')
    pool.close()  # 必须先close在join
    pool.join()  # 进程池中进程执行完毕后再关闭，如果注释掉，那么程序直接关闭。
    print('enddd')