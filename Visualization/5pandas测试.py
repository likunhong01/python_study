#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/12/20 13:55'
__author__ = 'likunkun'


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame(np.random.randn(1000, 4), columns=['A','B','C','D'])
df = df.cumsum()

# 绘制散点图
df.plot(alpha=0.7, linewidth=1.5)
plt.title('Pandas-Plot')
plt.show()

# 指定前三列绘制箱线图
df.iloc[:, 0:3].boxplot()
plt.show()

# 绘制直方图
df.hist(bins=20)
plt.show()

# -----------------------------------------------------------
# 更好看的直方图，把df改小一点,没有负数
df = pd.DataFrame(np.random.rand(10, 4), columns=['A','B','C','D'])
df.plot.bar()
plt.show()

# 改成水平放置，堆积的柱状图
df.plot.barh(stacked=True)
plt.show()

#散点图
df = pd.DataFrame(np.random.rand(100, 4), columns=['A','B','C','D'])
df.plot.scatter(x='A',y='B',s=df['C']*200)
plt.show()
