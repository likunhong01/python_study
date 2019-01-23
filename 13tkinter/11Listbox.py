#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/1/19 15:17'
__author__ = 'likunkun'

from tkinter import *
root = Tk()
theListbox = Listbox(root, setgrid = True, height = 15) # height可以设置高度
theListbox.pack()

somethings = ['巧克力','水果','饮料']

for item in somethings:
    theListbox.insert(END, item)

button1 = Button(root, text = '删除', command = lambda x = theListbox: x.delete(ACTIVE))
button1.pack()

mainloop()