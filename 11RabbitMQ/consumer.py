#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/10/11 18:37'
__author__ = 'likunkun'

import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)
channel = connection.channel()

#这里再次声明从那个队列去收消息（可以不写，但必须要有这个队列，不然会报错）
channel.queue_declare(queue='hello',
                      # durable=True  #durable=True为队列持续化
                      )

def callback(ch, method, properties, body):
    print('[x] 收到%r'%body)
    # 给队列发一个确认执行完的信息，否则消息会保存起来，不会被消费掉，会转给下个消费者
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)

channel.basic_consume(
    callback,
    queue='hello',
    # no_ack=True   #取消发送消息中断处理功能，不管有没有处理完，都不会给服务器端发确认
)

print('[*] Waiting for messages. Toexit press CTRL+C')
channel.start_consuming()