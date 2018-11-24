#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/8/14 17:25'
__author__ = 'Colby'

#copy文件用的
#高级的 文件、文件夹、压缩包 处理模块

import shutil

f1 = open('本节笔记',encoding='utf-8')
f2 = open('笔记2','w',encoding='utf-8')
shutil.copyfileobj(f1,f2)   #将文件内容拷贝到另一个文件中，可以部分内容

shutil.copyfile('笔记2','笔记3')    #复制
shutil.copymode()   #copy权限

shutil.copystat()   #拷贝状态的信息，包括：mode bits, atime, mtime, flags
shutil.copy()       #全copy

shutil.copy2()      #拷贝文件和状态信息

shutil.copytree()   #递归copy文件
shutil.rmtree()     #递归删除

shutil.move()       #移动文件

#打包
shutil.make_archive('base_name, format,...')   #创建压缩包并返回文件路径
'''
base_name： 压缩包的文件名，也可以是压缩包的路径。只是文件名时，则保存至当前目录，否则保存至指定路径，
如：www                        =>保存至当前路径
如：/Users/wupeiqi/www =>保存至/Users/wupeiqi/
format：	压缩包种类，“zip”, “tar”, “bztar”，“gztar”
root_dir：	要压缩的文件夹路径（默认当前目录）
owner：	用户，默认当前用户
group：	组，默认当前组
logger：	用于记录日志，通常是logging.Logger对象
'''