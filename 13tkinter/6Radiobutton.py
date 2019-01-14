#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/1/14 22:55'
__author__ = 'likunkun'

from tkinter import *

# 单选
root = Tk()
v = IntVar()
Radiobutton(root, text='One', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='Two', variable=v, value=2).pack(anchor=W)
Radiobutton(root, text='Three', variable=v, value=3).pack(anchor=W)

mainloop()