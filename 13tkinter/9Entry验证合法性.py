#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2019/1/19 13:40'
__author__ = 'likunkun'

# Entyr可以验证输入内容的合法性
# 通过设置validate，validatecommand，invalidcommand三个选项实现
# validate：
#   focus：当组件获得或失去焦点的时候验证
#   focusin：当组件获得焦点的时候验证
#   focusout：当组件失去焦点时候验证
#   key：当输入框被编辑的时候验证
#   all：当出现上面任一种情况的时候验证
#   none：关闭验证
#
# validatecommand选项指定一个验证函数，该验证函数只能返回true或者false，表示验证的结果
# invalidcommand在上面的函数false后调用
'''
from tkinter import *
root = Tk()

def test():
    if e1.get() == 'lkk':
        return True
    else:
        e1.delete(0,END)
        return False

def test2():
    print('test2调用')
    return True

v = StringVar()
e1 = Entry(root, textvariable = v, validate = 'focusout', validatecommand=test, invalidcommand=test2)
e2 = Entry(root)
e1.pack(padx = 10, pady = 10)
e2.pack(padx = 10 ,pady = 10)

mainloop()
'''

from tkinter import *
root = Tk()
v = StringVar()

def test(content, reason, name):
    if content == 'lkk':
        print(content, reason, name)
        return True
    else:
        print(content, reason, name)
        return False

testCMD = root.register(test)   # 调用register吧验证函数包装起来
e1 = Entry(root, textvariable = v, validate = 'focusout', validatecommand = (testCMD, '%P', '%v', '%W'))
e2 = Entry(root)
e1.pack()
e2.pack()

mainloop()
