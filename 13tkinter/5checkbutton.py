#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/1/12 22:12'
__author__ = 'likunkun'

from tkinter import *

root = Tk()

# 设置一个变量，表示该按钮是否被选中
v = IntVar()
c = Checkbutton(root, text='测试', variable=v)
c.pack()

# 如果被选中，那么v变为1，否则0
# 可以用各个Label标签展示01
l = Label(root, textvariable=v)
l.pack()


commends = ['李昆洪','李昆昆','lkk']
v = []
for c in commends:
    v.append(IntVar())
    b = Checkbutton(root, text=c, variable=v[-1])
    b.pack(anchor=W)

mainloop()