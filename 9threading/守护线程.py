#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/9/26 10:31'
__author__ = 'likunkun'


'''
守护线程：只要主线程执行完毕，不等其他线程，就退出程序
就是等待非守护线程执行完毕就退出
t.setDaemon(True)
一定要在start之前
'''