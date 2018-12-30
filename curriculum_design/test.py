# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)

# 这个是style的内置风格
style.use('fivethirtyeight')

# 多次使用figure函数可以绘制产生多个图，其中，图片号按顺序增加。
# 这里，要注意一个概念当前图和当前坐标。所有绘图操作仅对当前图和当前坐标有效.



# 你可以尝试下面这段代码，就可以理解figure的含义

# plt.figure(1) # 第一张图
# plt.subplot(211) # 第一张图中的第一张子图
# plt.plot([1,2,3])
# plt.subplot(212) # 第一张图中的第二张子图
# plt.plot([4,5,6])
# plt.figure(2) # 第二张图
# plt.plot([4,5,6]) # 默认创建子图subplot(111)
# plt.figure(1) # 切换到figure 1 ; 子图subplot(212)仍旧是当前图
# plt.subplot(211) # 令子图subplot(211)成为figure1的当前图
# plt.title('Easy as 1,2,3') # 添加subplot 211 的标题

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    graph_data = open('example.txt', 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []

    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(x)
            ys.append(y)

    ax1.clear()
    ax1.plot(xs, ys)

ani = animation.FuncAnimation(fig, animate, interval = 1000)

plt.show()
