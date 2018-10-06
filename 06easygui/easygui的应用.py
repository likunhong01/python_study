#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/10/6 22:26'
__author__ = 'likunkun'


'''--------------------------------------------------------------------'''
import easygui as g
import sys
import PIL #图像库，必须要安装，要不然不能显示图像
g.egdemo()

#msgbox()
g.msgbox('hello world!','标题','确认')

#choicebox()
g.choicebox('你相信我吗？',choices=['相信','不相信'])

#ccbox() 选择窗口
if g.ccbox('还要继续吗？',choices=['继续','不来了'],default_choice='继续',image='1.jpg'):
    g.msgbox('那就继续吧')
else:
    sys.exit(0)

#ynbox() 与ccbox一模一样，没有任何区别
if g.ynbox('还要继续吗？',choices=['继续','不来了'],default_choice='继续'):
    g.msgbox('那就继续吧')
else:
    sys.exit(0)

#buttonbox() 按钮框，显示一组定义好的按钮；当用户返回任意一个按钮时，buttonbox()返回按钮的文本内容
if '足球' == g.buttonbox('你喜欢什么运动？',title='运动类型调查',choices = ['篮球','排球','足球'],default_choice='足球'):
    g.msgbox('足球')
else:
    g.msgbox('other')

#indexbox()
#和buttonbox()基本相同，只是在点击按钮后，返回的是对应按钮的序号,序号也是从0开始的
if  2 == g.indexbox('你喜欢什么运动？',title='运动类型调查',choices = ['篮球','排球','足球'],default_choice='足球'):
    g.msgbox('足球')
else:
    g.msgbox('other')

#boolbox() 只有两个按钮，第一个按钮被选中返回1，否则返回0
if g.boolbox('还要继续吗？',choices=['是的','我放弃']):
    g.msgbox('继续前进')
else:
    g.msgbox('到此为止了')
    sys.exit(0)

#multchoicebox() 多选框
temp = g.multchoicebox('select some',choices=['A','B','C','D','E'])
g.msgbox(temp)

#enterbox() 让用户输入消息，返回字符串；默认情况下，自动去除首尾的空格，要保留的话，设置strip = False
temp = g.enterbox('请输入字符串')
g.msgbox(temp)

#integerbox() 输入一个有范围限制的整型，如果在范围之外，则要求重新输入
g.integerbox('输入一个整数',lowerbound=0,upperbound=100)

#multenterbox() 提供多个输入框，field是输入的项目；values是各个项目的默认值
temp = g.multenterbox('input',fields=['A','B','C','D'],values=['0','0','0','0'])
print(temp)

#输入密码的操作
#passwordbox()
#和enterbox()样式一样，不同的是用户输入的内容用‘*’显示出来，返回用户输入的字符串
ps = g.passwordbox('input password',image='1.jpg')
print(ps)

#multpasswordbox()
#跟multenterbox()使用相同的接口，但当它显示的时候，最后一个输入框显示为密码的形式
temp = g.multpasswordbox('input password',fields=['A','B','C','D'],values=['1','2','3','4'])
print(temp)

#textbox() 显示文本 text 可以是str、list、tuple类型，
# 默认以非等宽字体显示，使用codebox可以修改为等宽字体
g.textbox('显示文本',text=','.join('qwertyuiop'),codebox=1)

#codebox() 与textbox()作用相同，唯一不同是，codebox()默认以等宽字体显示
g.codebox('显示文本',text=','.join('qwertyuiop'))

#显示目录与文件
#提供了一些基本函数来让用户浏览文件系统，选择一个目录或者文件,
#diropenbox() default设置一个默认目录，返回一个完整的绝对路径，选择cancel则返回None
path = g.diropenbox('please select a dir',default='.')
print(path)

#fileopenbox()返回用户选择的文件名（绝对路径），否则返回None
temp = g.fileopenbox('select a file',default='./*.py')
print(temp)

#filesavebox() 让用户选择保存的路径，返回一个完整的路径，并不会真正的保存
temp = g.filesavebox('select a path',default='新建',filetypes=['*.txt','*.py'])
print(temp)

#记住用户的设置
#待解决，不是很懂

#捕获异常
#exceptionbox() #显示一个窗口，显示异常的具体原因
try:
    print('i love python')
    int('a') #产生异常
except:
    g.exceptionbox()