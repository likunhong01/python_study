#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/9/19 17:46'
__author__ = 'likunkun'
import gevent

def func1():
    print('11')
    gevent.sleep(2)
    print('12')

def func2():
    print('21')
    gevent.sleep(1)
    print(22)
    gevent.sleep(0.5)
    print(23)

def func3():
    print(31)
    gevent.sleep(0.5)
    print(32)

#11,21,31,32,22,23,12
gevent.joinall([
    gevent.spawn(func1),
    gevent.spawn(func2),
    gevent.spawn(func3),
])
'''

def A():
    print('a')
    B()
    print('aa')
    return

def B():
    print('b')
    C()
    print('bb')
    return

def C():
    print('c')
    return


A()
'''


def A():
    print(1)
    print(2)
    print(3)
def B():
    print('x')
    print('y')
    print('z')

