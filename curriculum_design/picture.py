#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/12/28 18:45'
__author__ = 'likunkun'

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import random
import threading
import time

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = ax.plot([], [],label='temperature')
tem = []

def init():
    ax.set_xlim(0, 20)
    ax.set_ylim(-50, 50)
    return ln,

def update(i):
    i = int(i)
    xdata.append(i)
    ydata.append(tem[i])
    ln.set_data(xdata, ydata)
    # time.sleep(1.05)
    return ln,

def whi():
    for x in range(20):
        i = random.randint(-40,40)
        tem.append(i)
        print(i)
        time.sleep(1)

threading.Thread(target=whi).start()

ani = animation.FuncAnimation(fig, update, frames=np.linspace(0,22,24),
                init_func=init, blit=False,interval=1000)

plt.show()
print(124124125)
# for a, b in zip(range(20), tem):
#         plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
#
# plt.show()




def last():
    x1 = list(range(20))
    y1 = tem
    plt.plot(x1, y1,  color='r',markerfacecolor='blue',marker='o')
    for a, b in zip(x1, y1):
        plt.text(a, b, (a,b),ha='center', va='bottom', fontsize=10)
    plt.show()

# with t1
# threading.Thread(target=last).start()