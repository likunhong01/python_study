#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/9/18 12:29'
__author__ = 'likunkun'

from multiprocessing import Process, Manager

def f(d, l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.append(1)
    # print(l)

if __name__ == '__main__':
    d = Manager().dict()  # 生成一个字典，可在多个进程间共享和传递
    l = Manager().list(range(5))  # 列表
    p_list = [] #进程列表
    for i in range(10):
        p = Process(target=f, args=(d, l))  #循环10次每次创建一个进程
        p.start()
        p_list.append(p)    #加入进程列表里
    for res in p_list:  #等所有进程结束
        res.join()
    print(d)
    print(l)
