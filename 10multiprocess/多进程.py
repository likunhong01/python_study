#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/9/18 11:56'
__author__ = 'likunkun'

# from multiprocessing import Process
import time ,os
import multiprocessing


def f(name):
    time.sleep(2)
    print('hello', name)
    print(os.getpid())
    print(os.getppid())


if __name__ == '__main__':
    p = multiprocessing.Process(target=f, args=('boy',))
    p.start()
    p.join()




import os


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    print("\n\n")


def f(name):
    info('\033[31;1mfunction f\033[0m')
    print('hello', name)

#在windows下用多进程一定要加下面这句话，他的作用是为了区分，你是主动执行这个脚本还是当做模块调用，如果导入的就不执行
if __name__ == '__main__':
    info('\033[32;1mmain process line\033[0m')
    p = multiprocessing.Process(target=f, args=('bob',))
    p.start()
    p.join()
