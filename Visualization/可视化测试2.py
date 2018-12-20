#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/12/19 11:25'
__author__ = 'likunkun'

import numpy as np
import matplotlib.pyplot as plt

# 解决中文问题
import matplotlib as mpl
mpl.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
mpl.rcParams['axes.unicode_minus'] = False

x = np.linspace(-2 , 2, 100)
y1  = np.cos(np.pi * x)
y2 = np.sin(np.pi * x)

# alpha参数表示透明度：0-1逐渐加深
# linewidth表示线条或者点的粗细
plt.plot(x, y1, 'go' , label=r"$y1=\cos(\pi \times x)$", alpha=0.8, linewidth=0.7)
plt.plot(x, y2, 'r-' , label=r"$y1=\sin(\pi \times x)$", alpha=0.8, linewidth=0.7)

plt.xlabel('x-axis')
plt.ylabel('y-axis')

# axis按照（xmin，xmax，ymin，ymax）的格式来箱子坐标轴的范围
# 设置坐标范围
plt.axis([-2.1, 2.1, -1.2, 1.2])

# 显示标签（在plot里用lable写了的用这个显示）
plt.legend()

# 显示网格
plt.grid(alpha=0.4)

plt.title('two plots', color= (0.1, 0.3, 0.5))
plt.show()