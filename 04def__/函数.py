#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG




#高阶函数
'''
def bar():
    print('bar')
def test(func):
    print(func)
    func()
test(bar)
'''


#嵌套函数
def a():
    print('a')
    def b():
        print('b')
        print('bbb')
    b() #调用b函数
a() #调用a函数
