#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/1/11 11:59'
__author__ = 'likunkun'

import tkinter as tk

class App:
    def __init__(self, root):
        # 创建一个frame框架，然后里面可以添加各种组件，可以进行分组
        frame = tk.Frame(root)
        frame.pack()
        frame.pack(side=tk.LEFT)    # 设置内容为左对齐
        frame.pack(side=tk.LEFT, padx=10, pady=10)    # 设置内容为左对齐,再向下、向右偏移10个单位

        # 创建一个按钮组件，fg是foreground前景色，bg是背景色
        self.hi_there = tk.Button(frame,text='打招呼', bg='white' ,fg='black', command=self.say_hi)
        self.hi_there.pack()

    # 按钮触发事件
    def say_hi(self):
        print("hello")

# 创建一个toplevel根窗口，把它作为参数实例化app对象
root = tk.Tk()
app = App(root)
# 开始
root.mainloop()

