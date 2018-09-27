#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/9/26 11:35'
__author__ = 'likunkun'

'''
class queue.Queue(maxsize=0) #先入先出
class queue.LifoQueue(maxsize=0) #后进先出（栈）
class queue.PriorityQueue(maxsize=0) #存储数据时可设置优先级的队列
'''

'''
import queue

q = queue.Queue()

for i in range(10):
    q.put(i)

while q:
    print(q.get())
'''

import queue
#栈
q = queue.LifoQueue()

for i in range(10):
    q.put(i)

while q:
    print(q.get())


