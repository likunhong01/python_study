#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/12/29 15:34'
__author__ = 'likunkun'

#服务器端
import random
import socket
import time
# 定义类型变量
server = socket.socket()
#监听哪个端口,绑定端口
server.bind(('localhost', 6969))
# 监听
server.listen(5)    #最大同时接入5个连接
while True:
    conn, addr = server.accept()
    count = 0;
    while True:
        temperature = random.randint(-40,40)
        conn.send(bytes(str(temperature).encode()))
        count += 1
        time.sleep(1)

server.close()
