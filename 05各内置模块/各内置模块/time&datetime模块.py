#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/8/14 12:35'
__author__ = 'Colby'


import time

time.time() #获取时间戳
time.sleep(1)#睡几秒
time.gmtime() #返回元祖，表示utc时间（标准时间）（早8小时），传入时间戳转换到标准时间
time.localtime()    #转换成本地时间，可传入时间戳。
time.localtime().tm_year    #取出年份

time.mktime()   #把元祖形式的转换成时间戳形式
time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())  #格式化字符串表示时间
time.strptime('2018-08-14 13:35:17',"%Y-%m-%d %H:%M:%S")    #按格式转换回元祖类型

time.asctime()  #传入元祖，默认当前时间，返回字符串'%a %b %d %H:%M:%S %Y'表示的时间
time.ctime()    #传入时间戳，转换成字符串'%a %b %d %H:%M:%S %Y'表示时间


import datetime

datetime.datetime.now() #当前时间
datetime.datetime.now() + datetime.timedelta(3)  #三天后时间
datetime.datetime.now().replace(minute=3, hour= 4)  #获取时间后修改时间



import time
print(time.strftime("%Z",time.localtime())) #格式化字符串表示时间
'''-%m-%d %H:%M:%S'''

