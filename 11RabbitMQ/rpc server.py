#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/10/17 13:36'
__author__ = 'likunkun'

import pika
import time

#正常建立连接
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


#收到消息，执行命令，返回结果
def on_request(ch, method, props, body):
    n = int(body)   #收到body

    print(" [.] fib(%s)" % n)
    response = fib(n)   #处理得到结果

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id= \
                                                         props.correlation_id), #返回了id
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)  #确保任务完成了


# channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')    #收消息

print(" [x] Awaiting RPC requests")
channel.start_consuming()