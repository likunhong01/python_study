#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/10/17 15:02'
__author__ = 'likunkun'

import redis


class RedisHelper:

    def __init__(self):
        self.__conn = redis.Redis(host='192.168.16.96')
        self.chan_sub = 'fm104.5'
        self.chan_pub = 'fm104.5'

    def public(self, msg):  #调用conn的publish方法
        self.__conn.publish(self.chan_pub, msg)
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()  #开始订阅，打开收音机
        pub.subscribe(self.chan_sub)    #调频道
        pub.parse_response()    #准备接收
        return pub
