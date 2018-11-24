#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/8/14 17:09'
__author__ = 'Colby'

import sys, time

sys.argv           #命令行参数List，第一个元素是程序本身路径
sys.exit(0)        #退出程序，正常退出时exit(0)
sys.version        #获取Python解释程序的版本信息
sys.maxint         #最大的Int值
sys.path           #返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.platform       #返回操作系统平台名称

sys.stdout.write('please:') #需要配合sys.stdout.flush()把写的刷出来
sys.stdout.flush()

val = sys.stdin.readline()[:-1] #把输入的东西赋值给val
print(val)

#模拟一个进度条
for i in range(20):
    sys.stdout.write("#")
    sys.stdout.flush()
    time.sleep(0.5)
