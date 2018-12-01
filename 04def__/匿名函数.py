#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG


#只调用一次的话，没必要单独写，写一个匿名函数，用完就释放
def sayhi(n):
    print(n)

sayhi(3)

#匿名函数只能写三元之内运算
(lambda n:print(n))(3)

calc = lambda n:print(n)
calc(5)


#在1-10中过滤出大于5的数据
filter(lambda n:n>5, range(10))

map(lambda n : n*n ,range(10))