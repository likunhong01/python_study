#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG

#高阶函数+嵌套函数=装饰器

import time

"""
'''装饰器，计算test花费时间'''
def timer(func):    #函数可以作为参数传进另一个函数（高阶函数），这里第一层传入一个函数
    def secend():   #第二层加入新的功能
        start_time = time.time();
        res = func()  #调用原来的函数（func()中：func代表传入的那个函数，右边写上一对小括号等于调用的意思），返回值用res接收
        end_time = time.time();
        print("运行时间为%s秒"%(end_time - start_time))   #打印耗时
        return res  #这里用res接收func的返回值并return，确保不遗漏返回值
    return secend

'''原函数'''
# @timer  #等价于这句话：test = timer(test)，也就是test= secend，现在test() = secend()
def test():
    time.sleep(1)
    print("this is test func")
    return 1

'''
timer（test）的返回值是secend，（不带括号），也就是新写出来的函数的内容的地址，包括了新的功能，赋值给原来的test替换掉
（函数即变量），在运行原来的test，就可以使用到装饰器的功能，并且调用test()的地方不用删除，只需要增加一句话，也不改变原
来函数里面的内容。但因为这样改动麻烦（要在所有调用过test的地方改），所以python给了一种方法：在test函数头加上一句：@timer，
在下面会介绍到。
'''
test = timer(test)
test()
"""

#带*不定参数装饰器
def timer(func):
    def secend(*args,**kwargs):
        start_time = time.time();
        res = func(*args,**kwargs)
        end_time = time.time();
        print("运行时间为%s秒"%(end_time - start_time))
        return res
    return secend

@timer  #等价于这句话：test = timer(test)，也就是test= secend，现在test() = secend()
def test():
    time.sleep(1)
    print("this is test func")

@timer  #testWithParameter = timer(testWithParameter)
def testWithParameter(name):
    time.sleep(1)
    print("这是有参数的函数，参数为：",name)

test()
testWithParameter('LIKUNKUN')
