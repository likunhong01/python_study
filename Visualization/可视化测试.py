#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/12/19 10:53'
__author__ = 'likunkun'

import numpy as np
import matplotlib.pyplot as plt

# -2 2表示横坐标从-2到2，100表示用100个点分布这个区间描述出图像，默认是50
x = np.linspace(-2, 2, 100)
y = np.cos(np.pi * x)

# x，y是自变量和因变量，r是红色，o表示用点表示出来,-表示用线
plt.plot(x,y,'r-')
plt.title(r"$y=\cos(\pi \times x$")
plt.show()

help(plt.plot)