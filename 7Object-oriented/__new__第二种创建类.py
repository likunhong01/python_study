#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/8/19 22:22'
__author__ = 'Colby'
'''
#第一种方法创建类
class A(object):

    def __init__(self, name):
        self.name = name

f = A("lkk")
print(type(f))  #打印f的类型，是A（我们写的class A）
print(type(A))    #不妨再打印一下A的类型，居然是type
'''
'''-----------------------------------------'''

#第二种方法创建类
def func(self):
    print('hello %s'%self.name)

def __init__(self,name,age):
    self.name = name
    self.age = age

#type('叫什么的类','继承谁','它里面有哪些方法')
#Foo = type('Foo',(), {'talk':func})
Foo = type('Foo', (object,), {'talk':func,
                              '__init__':__init__})


f = Foo('lkh','20')
f.talk()
print(type(Foo))

'''所以，type是类的类'''

class Foo(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def func(self):
        print('hello %s' % self.name)







