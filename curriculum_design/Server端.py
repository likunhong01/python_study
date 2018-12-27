#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG

__date__ = '2018/12/27 16:31'
__author__ = 'likunkun'

#服务器端
import random
import socket
import time
import threading


# 发回一个随机温度方法
def sendTemperature(conn):
    count = 0;
    while True:
        # data = conn.recv(1024)
        temperature = random.random(-20,40)
        conn.send(temperature) #返回处理后的数据
        count += 1
        time.sleep(1000)

# 定义类型变量
server = socket.socket()
#监听哪个端口,绑定端口
server.bind(('localhost', 6969))
# 监听
server.listen(5)    #最大同时接入5个连接
while True:
    conn, addr = server.accept()    #等连接进来发，返回的是conn是对方电话打过来的实例，addr是对方地址
    # print(conn)
    count = 0;
    while True:
        # data = conn.recv(1024)
        temperature = random.randint(-20,40)
        conn.send(temperature) #返回处理后的数据
        count += 1
        time.sleep(1000)
    # t = threading.Thread(target=sendTemperature(), args=(conn,))
    # t.start()

server.close()










