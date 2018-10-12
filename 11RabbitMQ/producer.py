#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/10/11 18:31'
__author__ = 'likunkun'

import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel = connection.channel()  #声明一个管道

#在管道里，再声明queue
channel.queue_declare(queue='hello',
                      # durable=True  #durable=True为队列持续化
                      )

#真正发消息，用管道发
channel.basic_publish(exchange='',
                      routing_key='hello',  #消息队列名称
                      body='Hello World!',  #消息内容
                      # properties=pika.BasicProperties(delivery_mode=2,) #消息持续化
)

print('[x] sent "Hello World!"')
connection.close()