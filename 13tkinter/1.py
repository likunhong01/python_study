#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/1/10 11:27'
__author__ = 'likunkun'

import tkinter as tk

# 创建一个主窗口，用于容纳整个GUI
root = tk.Tk()
#设置主窗口对象的标题栏
root.title("lkk")
# 添加一个label组件
# 可以显示文本，图标，图片
# 这里只显示文本
theLabel = tk.Label(root, text='窗口程序')
# 调用pack方法，用于自动调节组件自身的尺寸
theLabel.pack()
# 显示窗口
root.mainloop()
