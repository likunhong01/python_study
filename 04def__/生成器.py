#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG


#生成器generator
#方式一：
a = ( i * 2 for i in range(10))
print(a)    #打印a实际是一个生成器地址
print(a.__next__()) #打印第一个
print(a.__next__()) #打印第二个
for i in a:         #打印接下来的所有
    print(i)



#方式二：函数
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        #print(b)    #打印每个fib数
        yield b     #写了yield的函数，就是生成器，就不是函数了
        a, b = b, a + b
        n += 1
    return 'done'   #当超过了就会返回这个

a = fib(10) #赋值给a
print(a)    #打印a看一下，实际a是一个生成器（generator）地址

#使用方法一：
print(a.__next__())
print(a.__next__())
print(a.__next__()) #打印3次

#使用方法二：
for i in a: #循环打印之后的出来
    print(i)

#使用方法三：
while True:
    try:
        x = next(a)
        print(x)
    except StopIteration as e:  #当超出的时候抓住错误，并显示生成器的return值
        print(e.value)
        break