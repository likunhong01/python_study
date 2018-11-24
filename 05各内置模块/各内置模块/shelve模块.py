#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/8/14 18:15'
__author__ = 'Colby'

import datetime

import shelve
#shelve模块是一个简单的k,v将内存数据通过文件持久化的模块，可以持久化任何pickle可支持的python数据格式

#写入
d = shelve.open('shelve_test')  # 打开一个文件

info = {'age':22, 'job':'it'}
name = ['lkh','lkk','wangwu']
d['name'] = name
d['info'] = info
d['date'] = datetime.datetime.now();
d.close()

#读
d = shelve.open('shelve_test')
d.get('name')
d.get('info')
d.get('date')



