#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/1/19 16:53'
__author__ = 'likunkun'

from tkinter import *

root = Tk()
text = Text(root, width = 30 , height = 10)
text.pack()
# INSTER索引表示插入光标当前的位置
text.insert(INSERT, 'hello\n')
text.insert(END, 'lkk')
photo = PhotoImage(file='photo.jpg')

def show():
    print('aaaaaaaaa')  # 可以出文字
    text.image_create(END, image=photo) # 可以出图

b1 = Button(text, text='点我', command=show)  # 点击之后出反应
text.window_create(INSERT, window=b1)
mainloop()