#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/8/17 11:43'
__author__ = 'Colby'

import easygui as gui

gui.msgbox('欢迎到这个选择界面')
while True:
    mes = '你现在想吃什么？'
    title = '选择午餐'
    choices = ['烤鱼','汉堡','炸鸡','啤酒']
    people_choice = gui.choicebox(mes,title,choices)
    mes = '你吃了' + str(people_choice) + '！你还要继续吃吗？？？'
    choices = ['要！', '不吃了，吃不下了']
    a = gui.ccbox(mes, '请选择', choices)
    if a:
        gui.msgbox('那就继续吃吧')
    else:
        exit(0)

