#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/10/12 16:38'
__author__ = 'likunkun'

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

#定义exchange，类型必须是fanout，而且他是一个实时广播，必须都同时在线才可以收到，不会保存
channel.exchange_declare(exchange='logs', type='fanout')

message = "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()