#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/8/16 15:49'
__author__ = 'Colby'

class Dog:
    def __init__(self, name):
        self.name = name
    def bulk(self):
        print("%s汪汪汪"%self.name)

dog1 = Dog('1hao')
dog1.bulk()