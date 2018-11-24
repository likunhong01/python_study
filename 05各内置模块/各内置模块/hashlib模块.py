#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/8/14 22:10'
__author__ = 'Colby'
'''
import hashlib
#用于加密相关的操作，3.x里代替了md5模块和sha模块，主要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法

m = hashlib.md5()
m.update("Hello啥啊啊啊啊".encode(encoding='utf-8'))
m.update("It's me".encode(encoding='utf-8'))
print(m.digest())
m.update("It's been a long time since last time we ...".encode(encoding='utf-8'))

print(m.digest())  # 2进制格式hash
print(len(m.hexdigest()))  # 16进制格式hash

'''
#------------------------------------------------------------------#
import hashlib

# ######## md5 ########
hash = hashlib.md5()
hash.update('admin'.encode(encoding='utf-8'))
print(hash.hexdigest())

# ######## sha1 ########
hash = hashlib.sha1()
hash.update('admin'.encode(encoding='utf-8'))
print(hash.hexdigest())

# ######## sha256 ########
hash = hashlib.sha256()
hash.update('admin'.encode(encoding='utf-8'))
print(hash.hexdigest())

# ######## sha384 ########
hash = hashlib.sha384()
hash.update('admin'.encode(encoding='utf-8'))
print(hash.hexdigest())

# ######## sha512 ########
hash = hashlib.sha512()
hash.update('admin'.encode(encoding='utf-8'))
print(hash.hexdigest())


#--------------------------------------------------
import hmac
h = hmac.new(b'123', '你是二百五'.encode(encoding='utf-8'))
print(h.hexdigest())