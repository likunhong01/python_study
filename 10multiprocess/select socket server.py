#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/10/7 16:17'
__author__ = 'likunkun'

import select
import socket
import queue

server = socket.socket()
server.bind(('localhost',9000))
server.listen(1000)

server.setblocking(False)   #设置非阻塞模式
#accept不会堵塞了，没连接会报错

inputs = [server,] #监测的列表
outputs = []    #返回的连接列表
msg_dic = {}    #消息队列字典

while True:
    readable, writeable, exceptional = select.select(inputs, outputs, inputs)
    for r in readable:
        if r is server:  # 如果来的是新连接（server活跃）
            conn, addr = server.accept()
            print('来了个新连接：', addr)
            inputs.append(conn)
            msg_dic[conn] = queue.Queue()
        else:  # 来的是连接
            data = r.recv(1024)
            print('收到', data)
            msg_dic[r].put(data)
            outputs.append(r)

    for w in writeable:  # 要返回给客户端的连接列表
        data_w = msg_dic[w].get()  # 取得消息队列中的元素
        print(data_w)
        w.send(data_w)  # 返回数据
        print('send done')
        outputs.remove(w)  # 确保下次循环的时候writeable,不返回这个已经处理完的连接了

    for e in exceptional:
        if e in outputs:
            outputs.remove(e)  # 如果在返回列表里，就删掉outputs里的e
        inputs.remove(e)  # 删除检测列表里的e
        del msg_dic[e]  # 删除消息队列





