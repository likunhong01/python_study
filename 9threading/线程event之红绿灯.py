#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/9/12 17:46'
__author__ = 'likunkun'

'''红绿灯'''
import threading,time

#event就是一个在线程里的标志，随时可以切换
event = threading.Event()

def Lighter():
    count=0
    event.set()
    while True:
        if count > 3 and count <= 6:  #30-60秒为红灯
            event.clear()   #清除，变成红灯
            print("\033[41;1m红灯亮\033[0m")
        elif count > 6:
            event.set() #变成绿灯
            count = 0   #重置计时器
        else:
            print("\033[42;1m绿灯亮\033[0m")
        time.sleep(1);
        count += 1

def Car(name):
    while True:
        if event.is_set():
            print(name,'开车')
            time.sleep(1)
        else:
            print(name,'停车')
            time.sleep(1)

light = threading.Thread(target=Lighter,)
light.start()
car = threading.Thread(target=Car,args=('宝马',))
car.start()