#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/8/16 22:02'
__author__ = 'Colby'

class Animal(object):
    def __init__(self, name):  # Constructor of the class
        self.name = name

    def talk(self):  # 抽象方法，仅由约定定义
        print(self.name,'叫')

    def animal_talk(obj):  # 多态
        obj.talk()
        # obj.jiao()

class Cat(Animal):
    def jiao(self):
        print('%s: 喵喵喵!' % self.name)

class Dog(Animal):
    def talk(self):
        print('%s: 汪！汪！汪！' % self.name)

a = Cat('a')
Animal.animal_talk(a)    #a: 汪！汪！汪！

x = Animal('dog')
x.talk()    #dog 叫