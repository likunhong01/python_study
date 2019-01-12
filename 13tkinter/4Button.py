#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/1/12 21:37'
__author__ = 'likunkun'

from tkinter import *

def callback():
    var.set("hehe")

root = Tk()
frame1 = Frame(root)
frame2 = Frame(root)

# 创建一个Label对象
var = StringVar()
var.set("aaaaaaaaaaaaaaaaaaaaaa")
textLabel = Label(frame1, textvariable=var, justify=LEFT)
textLabel.pack(side=LEFT)

# 按钮
theButton = Button(frame2, text="bbbbbbbbbbb", command=callback)
theButton.pack()

frame1.pack(padx=10, pady=10)
frame2.pack(padx=10, pady=10)

mainloop()