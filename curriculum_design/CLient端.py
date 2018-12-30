#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/12/27 16:32'
__author__ = 'likunkun'

#客户端
import socket
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import threading
import time

#动态作图
fig, ax = plt.subplots()    #新建一个画布
xdata, ydata = [], []   # 横坐标和纵坐标
ln, = ax.plot([], [],label='temperature',markerfacecolor='blue',marker='o') # 直线的样式
tem = []    # 传过来的温度的列表

client = socket.socket() #声明socket类型，同时生成socket连接对象
client.connect(('localhost',6969))  # 连接端口

# 画布初始化函数
def init():
    ax.set_xlim(0, 100)
    ax.set_ylim(-50, 50)
    return ln,

# 更新函数，每次画面刷新调用这个函数实现更新
def update(i):
    i = int(i)  # 确保i是int类型
    xdata.append(i) # 把x和y加入到队列中
    ydata.append(tem[i])
    ln.set_data(xdata, ydata)   # 设置x，y
    return ln,

# 客户端接受数据的方法，用线程启动
def clientT():
    count = 0
    while count < 100:
        data = client.recv(1024)
        i = data.decode()
        tem.append(int(i))
        # print(tem)
        count += 1

# 启动一个线程来接受数据，存入tem列表
t1 = threading.Thread(target=clientT)
t1.start()

# 启动动画
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0,99,20),
                              init_func=init, blit=False,interval=1000)
# 展示
plt.show()

t1.join()   # 等线程运行结束
client.close()  #关闭端口