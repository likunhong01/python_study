#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/9/18 12:23'
__author__ = 'likunkun'

'''管道pipe'''
from multiprocessing import Process, Pipe

def f(conn):
    conn.send('hello')  #发送hello
    print(conn.recv())  #收到牛逼
    conn.close()        #关闭

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()    #管道会产生两个返回值
    p = Process(target=f, args=(child_conn,))   #创建一个子进程
    p.start()
    print(parent_conn.recv())  #收到'hello'"
    parent_conn.send('牛逼')  #发送牛逼
    p.join()
