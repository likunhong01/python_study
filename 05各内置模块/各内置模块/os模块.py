#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/8/14 16:00'
__author__ = 'Colby'

import os

os.getcwd() #获取当前路径
os.chdir('C:\\Users')  #切换目录
os.chdir(r'C:\Users')  #切换目录（推荐）
os.curdir   #返回当前目录
os.pardir   #返回上一目录

os.makedirs(r'C:\a\b\c\d')   #递归创建（当目录不存在的时候）
os.removedirs(r'C:\a\b\c\d') #删除路径的文件，如果上一级是空也一起删了

os.mkdir(r'C:\a\b\c\d') #建立目录，如果没有父目录则不能创建
os.rmdir(r'C:\a\b\c\d') #删除目录，不删除父（空的）的目录

os.listdir('..')    #返回目录里的东西
os.remove('')   #删除一个文件
os.rename() #重命名文件

os.stat('path/filename')  #获取文件/目录信息


os.sep    #输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
os.linesep    #输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
os.pathsep    #输出用于分割文件路径的字符串
os.environ  #查看系统环境变量

os.name    #输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
os.system("bash command")  #运行shell命令，直接显示

os.path.abspath('path')  #返回path规范化的绝对路径
os.path.split('path')  #将path分割成目录和文件名二元组返回
os.path.dirname('path')  #返回path的目录。其实就是os.path.split(path)的第一个元素
os.path.basename('path')  #返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
os.path.exists('path')  #如果path存在，返回True；如果path不存在，返回False
os.path.isabs('path')  #如果path是绝对路径，返回True
os.path.isfile('path')  #如果path是一个存在的文件，返回True。否则返回False
os.path.isdir('path')  #如果path是一个存在的目录，则返回True。否则返回False
os.path.join('path1[, path2[, ...]]')  #将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime('path')  #返回path所指向的文件或者目录的最后存取时间
os.path.getmtime('path')  #返回path所指向的文件或者目录的最后修改时间



