#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/1/19 17:22'
__author__ = 'likunkun'

from tkinter import *
root = Tk()
w = Canvas(root, width = 200, height = 100)
w.pack()
# 黄色线
w.create_line(0, 50, 200, 50, fill= 'yellow')
w.create_line(100, 0, 100, 100, fill= 'red', dash = (4,4))
w.create_line(50, 25, 150, 75, fill= 'blue')

mainloop()