#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/10/19 17:51'
__author__ = 'likunkun'

import pymysql

# 创建连接
'''host：主机地址；
port：mysql默认端口3306；
user：数据库用户名一般root；
passwd：安装数据库你设置的密码
db：要操作的数据库的名称（第一次要在mysql的命令行里先创建自己的数据库）
charset：编码格式'''
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='35278479', db= 'us_states', charset='utf8')

# 创建游标，相当于mysql命令行的那个光标，可以输入sql语句的地方
cursor = conn.cursor()

# 执行SQL，并返回收影响行数
#创建states表格，有id，state，population这3个列
effect_row = cursor.execute("CREATE TABLE states (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, state CHAR(25), population INT(9))")
print(effect_row)

#插入数据
effect_row = cursor.execute("INSERT into states (id, state, population) values (1, '加州', 5)")
print(effect_row)

effect_row = cursor.execute("select * from states")
print(effect_row)

#接受一行
row_1 = cursor.fetchone()
print(row_1)

#接受n行
row_1 = cursor.fetchone(5)
print(row_1)

#接受全部行
row_all = cursor.fetchall()
print(row_all)

# 提交，不然无法保存新建或者修改的数据
conn.commit()

# 关闭游标
cursor.close()

# 关闭连接
conn.close()