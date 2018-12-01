#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG

import json

#主要用于不同语言之间的交互
#只能处理简单的，处理复杂的用pickle

#字典info
info = {
    'name' : 'likunhong',
    'age' : 20
}

json.dumps(info) #把字典转换成可储存字符串

#可以存到硬盘上，保留格式的存
x = json.dumps(info)

#从硬盘上取出，仍有之前的格式，这里是字典
y = json.loads(x)
print(y['age'])


import pickle
'只能在python里存取，可以存取高级信息'

info = {
    'name' : 'likunhong',
    'age' : 20
}
f = open("test.text",'wb')
pickle.dump(info,f) #等价于f.write(pickle.dumps(info))
data = pickle.load(f) #等价于data = pickle.loads(f.read())
'''语法和json基本一致'''


