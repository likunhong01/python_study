#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG


import time

def consumer(name):
    while True:
        food = yield
        print('%s吃了%s号食物'%(name, food))

def producter(name):
    print('%s开始做吃的了'%name)
    c1 = consumer('a')
    c2 = consumer('b')
    c1.__next__()   #第一次要next一下才能走到生成器的yield位置
    c2.__next__()
    for i in range(100):
        print('----------------------')
        print('做好了%s号吃的'%i)
        c1.send(i)
        c2.send(i)
        time.sleep(1)
    c1.close()
    c2.close()

producter('lkh')