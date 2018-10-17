#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/10/17 13:31'
__author__ = 'likunkun'

import pika
import uuid , time


class FibonacciRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:    #收到了返回的随机字符串，当返回的id和本地的id是一样的，证明数据是对的
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())    #随机字符串id（有规则的字符串）
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue', #消息队列名称
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,    #让服务器端执行完后，吧结果返回到这个queue里
                                       correlation_id=self.corr_id, #吧随机的id发给服务器端
                                   ),
                                   body=str(n))

        while self.response is None:
            self.connection.process_data_events()   #非阻塞版的start_consuming
            print('no msg……')
            time.sleep(0.5)
        return int(self.response)


fibonacci_rpc = FibonacciRpcClient()

print(" [x] Requesting fib(30)")
response = fibonacci_rpc.call(30)
print(" [.] Got %r" % response)