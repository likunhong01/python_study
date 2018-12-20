#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/12/20 10:28'
__author__ = 'likunkun'

import numpy as np
import matplotlib.pyplot as plt

# 绘制子图
plt.style.use('ggplot') # 设置绘图风格
# print(plt.style.available)  #查看其它风格

x = np.linspace(-2, 2, 100)
# 都是πx
y1 = np.sin(np.pi * x)
y2 = np.cos(np.pi * x)
y3 = np.tan(np.pi * x)

y4 = x

# 22表示子图是2行2列，一共4个子图，1表示这个做第一个子图
plt.subplot(221)
plt.plot(x, y1)

plt.subplot(222)
plt.plot(x, y2)

plt.subplot(223)
plt.plot(x, y3)

plt.subplot(224)
plt.plot(x, y4)

plt.show()
