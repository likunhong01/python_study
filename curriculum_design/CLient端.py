
#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/12/27 16:32'
__author__ = 'likunkun'


#客户端
import socket
import time

client = socket.socket() #声明socket类型，同时生成socket连接对象
client.connect(('localhost',6969))
# 当要不停的发送接受
while True:
    # msg = input('>>').strip()   #发送消息
    # client.send(msg.encode('utf_8'))
    data = client.recv(1024)
    print('recv:', data.decode())
    time.sleep(1000)

client.close()

















