#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/9/18 12:00'
__author__ = 'likunkun'

from multiprocessing import Process, Queue
#注意这里要import Queue，之后的使用相当于备份一个queue，并且是一个同步的queue

def f(q):
    q.put(25)

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    '''实现主进程和子进程的通信，放入同一个队列中'''
    p.start()
    print(q.get())
    p.join()