#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/8/16 16:10'
__author__ = 'Colby'


class Role(object):
    n = 123 #类变量
    name = 'likunkun'   #如果实例本身没有，就去类变量里面找
    def __init__(self, name, role, weapon, life_value=100, money=15000):
        #构造函数
        #在实例化时做一些类的初始化工作
        #self就是对象本身
        self.name = name    #实例变量（静态属性），赋值给实例，作用域是实例本身
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.__life_value = life_value  #私有属性加__，要定义方法，才可以访问
        self.money = money

    def __ppp(self):
        print('这是私有方法，加__')

    def show_status(self):
        print('在内部才可以使用私有属性或者方法：life：%s'%self.__life_value)

    def __del__(self):
        print("析构函数")

    def shot(self): #类的方法，功能（动态属性）
        print("shooting...")

    def got_shot(self):
        print("ah...,I got shot...")

    def buy_gun(self, gun_name):
        print("just bought %s" % gun_name)


#把一个类变成一个具体的对象的过程叫实例化
r1 = Role('Alex', 'police', 'AK47') #生成一个角色
r2 = Role('Jack', 'terrorist', 'B22')  #生成一个角色


#实例化的过程等于下面
r1 = Role(r1,'lkk', 'police', 'ak47')
r1.name = 'lkk'
r1.role = 'police'
r1.weapon = 'ak47'
r1.buy_gun()    #Role.buy_gun(r1)

#给r1加上一个属性
r1.bullet_prove = True

#删掉r1的武器属性
del r1.weapon

#改类变量
r1.n = '改变了的类变量'    #相当于创建一个新的n在r1里，不影响r2
Role.n = '123456'   #直接把类变量内部改了
