#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/8/21 10:51'
__author__ = 'Colby'

#客户端
import socket


"""
#声明socket类型，同时生成socket连接对象
client = socket.socket()

#连接
client.connect(('localhost'),6969)

#-----------------------------
#发数据
client.send(b'hello world')
client.send('你好'.encode('utf-8')) #如果要发中文
#所有数据都要用bytes发送

#接受服务器端返回
data = client.recv(1024)    #1024字节
print('recv:',data)
#------------------------------
"""


client = socket.socket() #声明socket类型，同时生成socket连接对象
client.connect(('localhost',6969))
# 当要不停的发送接受
while True:
    msg = input('>>').strip()   #发送消息

    client.send(msg.encode('utf_8'))
    data = client.recv(1024)
    print('recv:', data.decode())

client.close()

















