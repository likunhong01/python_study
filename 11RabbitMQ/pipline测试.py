#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/10/17 14:46'
__author__ = 'likunkun'

import redis, time

pool = redis.ConnectionPool(host='localhost', port=6379)

r = redis.Redis(connection_pool=pool)

# pipe = r.pipeline(transaction=False)
# pipe = r.pipeline(transaction=True)

#这样的效果是name和role是一起最后执行的
pipe = r.pipiline()
pipe.set('name', 'alex')
time.sleep(5)
pipe.set('role', 'sb')

pipe.execute()