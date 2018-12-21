#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/12/20 10:52'
__author__ = 'likunkun'

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 500)
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)

fig, ax = plt.subplots()
ax.fill(x, y)
plt.show()