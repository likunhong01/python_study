#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/8/14 14:23'
__author__ = 'Colby'

import random

random.random() #随机0-1的浮点数

random.uniform(1,3) #随机1-3的浮点数

random.randint(1,5) #1234随机出一个
random.randrange(3) #包含头不包含尾
random.choice('asdlkga') #可以传入序列、字符串、列表，随机字符
random.sample('12345',2)    #随机返回前两个

#洗牌
puke = [1, 2, 3, 4, 5]  #有序数列
random.shuffle([1, 2, 3, 4, 5])    #把puke打乱


#生成随机验证码
checkCode = ''
long = 5
for i in range(4):

    checkCode += str(i)

print(checkCode)
