#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/12/29 15:34'
__author__ = 'likunkun'

import socket,time

client = socket.socket() #声明socket类型，同时生成socket连接对象
client.connect(('localhost',6969))
tem = []

count = 0
while True:
    data = client.recv(1024)
    i = data.decode()
    print(i)
    tem.append(i)
    print(tem)
    count += 1