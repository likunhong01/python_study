#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/1/19 14:18'
__author__ = 'likunkun'

from tkinter import *
root = Tk()
frame = Frame(root)
frame.pack(padx = 10, pady = 10)
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()

def test(content):
    if content.isdigit():
        return True
    else:
        return False

testCMD = root.register(test)
Entry(frame, textvariable = v1, width = 10, validate = 'key', validatecommand=(testCMD,'%P')).grid(row = 0, column=0)
Label(frame, text = '+').grid(row=0, column=1)
Entry(frame, textvariable = v2, width = 10, validate = 'key', validatecommand=(testCMD,'%P')).grid(row = 0, column=2)
Label(frame, text = '=').grid(row=0, column=3)
Entry(frame, textvariable = v3, width = 10, validate = 'key', validatecommand=(testCMD,'%P')).grid(row = 0, column=4)


def calc():
    result = int(v1.get()) + int(v2.get())
    v3.set(result)

Button(frame, text='计算结果', command=calc).grid(row = 1, column = 2, pady = 10)

mainloop()