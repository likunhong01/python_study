#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG


#普通列表
a = [1,2,3]
print(a)

#列表生成式
a = [i * 2 for i in range(10)]
print(a)

'''上面列表生成式的一行代码等价于下面3行'''
a = []
for i in range(10):
    a.append(i*2)
print(a)