#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/8/13 21:37'
__author__ = 'Colby'

import os,sys

# import module_name			#导入一个模块
# import module_name, module_name2	    #导入多个模块
# from module_name import *	#导入module_name里所有的东西（不建议使用，相当于把代码复制过来）
# from module_name import m1,m2,m3	#导入多个方法
# from module_name import logger as logger_name	#当logger方法名称发生重复时，重命名导入的logger方法
#
# def logger():
#     print('模块')
#
# logger()
# logger_name()


#import本质
import module_name
#相当于把module_name里的代码解释了一遍，然后赋值给变量module_name
#等于module_name = 那里面的所有代码

from module_name import name
#把定义name的代码复制过来，就是把name = ‘lkh’复制过来


#获取路径
x = os.path.dirname(os.path.abspath(__file__))
print(x)