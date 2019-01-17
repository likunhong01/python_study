#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/1/17 20:01'
__author__ = 'likunkun'

# 输入框，

from tkinter import *

root = Tk()
e = Entry(root)
e.pack(padx=20, pady=20)
e.delete(0, END)
e.insert(0, '默认文本')

mainloop()