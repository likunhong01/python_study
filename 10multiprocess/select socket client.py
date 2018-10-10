#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/10/9 12:47'
__author__ = 'likunkun'

import socket

HOST = 'localhost'
PORT = 9000

s = socket.socket()
s.connect((HOST,PORT))

while True:
    msg = bytes(input('>>:'), encoding='utf8')
    s.sendall(msg)
    data = s.recv(1024)
    print('收到',data)