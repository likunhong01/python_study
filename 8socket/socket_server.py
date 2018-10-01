#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/8/21 10:56'
__author__ = 'Colby'

#服务器端

import socket

"""
server = socket.socket()

#监听哪个端口,绑定端口
server.bind(('localhost', 6969))

#监听
server.listen()

#-----------------------------------
#等wait
print('开始等')
conn,addr = server.accept() #conn是对方电话打过来的实例，addr是对方地址
#coon就是客户端连过来而在服务器端为其生成的一个连接实例
print('来了')

#接受数据
data = conn.recv(1024)  #谁给你发过来，就接受谁
print('recv:',data )

#发送
conn.send(data.upper())
#------------------------------------
"""

# 定义类型变量
server = socket.socket()
#监听哪个端口,绑定端口
server.bind(('localhost', 6969))
# 监听
server.listen(5)    #最大等待5个人
#如果要不停的接受
while True:
    conn, addr = server.accept()    #等连接进来发，返回的是conn是对方电话打过来的实例，addr是对方地址

    count = 0
    #实现不止说一句就断开
    while True:
        data = conn.recv(1024)
        if not data and count > 10:
            print('对方未发送信息，断开。')
            break;
        # print('recv:', data)
        conn.send(data.upper()) #返回处理后的数据
        count+=1

server.close()




