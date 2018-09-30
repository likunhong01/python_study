#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/9/19 17:54'
__author__ = 'likunkun'

#要写一下爬虫
from urllib import request
import gevent,time,sys
from gevent import monkey

monkey.patch_all()

def climb(url):
    print('get %s'%url)
    resp = request.urlopen(url)
    data = resp.read()
    return data

url = 'https://blog.csdn.net/likunkun__/article/details/82793785'
neirong = climb(url)
print(neirong)

