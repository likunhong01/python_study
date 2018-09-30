#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/9/29 14:53'
__author__ = 'likunkun'

from greenlet import greenlet

def f1():
    print(12)
    gr2.switch()
    print(12)

def f2():
    print(21)
    gr1.switch()
    print(22)

gr1 = greenlet(f1)
gr2 = greenlet(f2)

gr1.switch()