#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/10/20 14:28'
__author__ = 'likunkun'

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

#创建连接
'''什么数据库+数据库的包：//用户名：密码@主机/数据库名称（db）'''
engine = create_engine("mysql+pymysql://root:35278479@localhost/us_states",
                       encoding='utf-8', echo=False) #echo表示是否打印所有操作信息

Base = declarative_base()  # 生成orm基类

#表的类，表的结构
class User(Base):   #继承基类
    __tablename__ = 'user'  # 表名
    #下面3个是列
    id = Column(Integer, primary_key=True)  #column是导入的
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return "<%s name:%s>" % (self.id, self.name)


Session_class = sessionmaker(bind=engine)  #返回的是类，创建与数据库的会话session类 ,这里返回给session的是个class,不是实例
Session = Session_class()  #这里再实例化，生成session实例，这个session就和pymysql里的cursor一样

'''创建表结构'''
# Base.metadata.create_all(engine)


'''插入数据'''
# #这里就是面向对象的形式创建每一行的数据了
# user_obj = User(name="lkk", password="lkk111")  # 生成你要创建的数据对象1
# user_obj2 = User(name="lihua", password="lihua111")  # 生成你要创建的数据对象2
# print(user_obj.name, user_obj.id)  # 此时还没创建对象，打印一下id发现还是None
#
# Session.add(user_obj)  # 把要创建的数据对象添加到这个session里， 一会统一创建
# Session.add(user_obj2)
#
# print(user_obj.name, user_obj.id)  # 此时也依然还没创建
#
# Session.commit()  # 现此才统一提交，创建（插入）数据



'''查数据'''
# data = Session.query(User).filter_by().all()    #取全部
# data = Session.query(User).filter_by().first()  #取第一个
# data = Session.query(User).filter(User.id > 2).all()  #取id>2的
# data = Session.query(User).filter(User.id > 2).filter(User.id < 4).all()  #取4>id>2的
# print(data)


'''修改数据'''
# data = Session.query(User).filter(User.id == 2).all()  #取id=2的
# #单改一个属性
# data.name = 'lkk1'  #现在可以改名字了


'''回滚'''
# my_user = Session.query(User).filter_by(id=1).first()
# my_user.name = "Jack"
#
# fake_user = User(name='Rain', password='12345')
# Session.add(fake_user)
#
# print(Session.query(User).filter(User.name.in_(['Jack', 'rain'])).all())  # 这时看session里有你刚添加和修改的数据
#
# Session.rollback()  # 此时rollback一下
#
# print(Session.query(User).filter(User.name.in_(['Jack', 'rain'])).all())  # 再查就发现刚才添加的数据没有了。

'''统计和分组'''
# from sqlalchemy import func
# print(Session.query(User).filter(User.name.like("lk%")).count())    #查找表格中lk开头的人出现多少次
# print(Session.query(User.name, func.count(User.name)).group_by(User.name).all() )   #统计每个name出现多少次



'''删除'''
Session.query(User).filter(User.id > 2).delete()
Session.commit()



'''连表查询'''
# ret = Session.query(User, Favor).filter(User.id == Favor.id).all()
#
# ret = Session.query(Person).join(Favor).all()
#
# ret = Session.query(Person).join(Favor, isouter=True).all()

