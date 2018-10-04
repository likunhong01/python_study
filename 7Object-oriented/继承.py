#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/8/16 20:04'
__author__ = 'Colby'

# class People1:  #旧式类写法
class People2(object):   #新式类写法（python3）
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('eat');

    def talk(self):
        print('talk')

    def sleep(self):
        print('sleep')

class Relation(object):

    def make_friends(self,obj):
        print('%s和%s成了好朋友'%(self.name,obj.name))

class Man(People, Relation):
    #对构造函数进行重构
    def __init__(self,name,age,money):
        #People.__init__(self,name,age)
        super(Man,self).__init__(name,age)
        self.money = money

    def work(self):
        print('man work')

    #重构sleep方法
    def sleep(self):
        print('man sleep')

class Women(People, Relation):

    def get_babay(self):
        print('women get baby')

man = Man('man', 20, 100)
women = Women('women' , 20)

man.make_friends(women)





