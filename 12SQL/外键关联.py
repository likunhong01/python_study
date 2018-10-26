#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/10/24 10:29'
__author__ = 'likunkun'

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker,relationship

#创建连接
'''什么数据库+数据库的包：//用户名：密码@主机/数据库名称（db）'''
engine = create_engine("mysql+pymysql://root:35278479@localhost/us_states?charset=utf8",    #如果要中文要加入后面charset
                       encoding='utf-8', echo=False) #echo打印所有信息

Base = declarative_base()  # 生成orm基类

#表的类，表的结构
class Student(Base):   #继承基类
    __tablename__ = 'student'  # 表名
    #下面2个是列
    id = Column(Integer, primary_key=True)  #column是导入的
    name = Column(String(32))

    def __repr__(self):
        return "<序号：%s，名字:%s>" % (self.id, self.name)

class StudyRecord(Base):
    __tablename__ = "study_record"
    id = Column(Integer,nullable=False,primary_key=True)
    day = Column(Integer,nullable=False)
    status = Column(String(32),nullable=False)
    stu_id = Column(Integer,ForeignKey('student.id'))

    #这里允许你在Student表里通过backref字段反向查出所有它在addresses表里的关联项
    #在内存里吧两个class关联起来，查询student表里的内容时候，用：结果.study_record  可以通过外键的映射关系，找到这个表里跟查询结果有关的内容，并按照此类的repr方法打印
    student = relationship("Student",backref='study_record')

    def __repr__(self):
        return "<记录号：%s，日期:%s，名字:%s>\n" %(self.id, self.day, self.student.name)

# Base.metadata.create_all(engine)  #提交创建表格

Session_class = sessionmaker(bind=engine)  #返回的是类，创建与数据库的会话session类 ,这里返回给session的是个class,不是实例
Session = Session_class()  #这里再实例化，生成session实例，这个session就和pymysql里的cursor一样

# s1 = Student(name='a')
# s2 = Student(name='b')
# s3 = Student(name='c')
# s4 = Student(name='d')

# study_obj1 = StudyRecord(day=1,status='yes',stu_id=1)
# study_obj2 = StudyRecord(day=2,status='no',stu_id=1)
# study_obj3 = StudyRecord(day=3,status='yes',stu_id=1)
# study_obj4 = StudyRecord(day=4,status='yes',stu_id=2)

# Session.add_all([s1,s2,s3,s4])
# Session.add_all([study_obj1,study_obj2,study_obj3,study_obj4])


stu_obj = Session.query(Student).filter(Student.name == 'a').first()
print(stu_obj)
print(stu_obj.study_record)

Session.commit()


'''多外键关联'''
from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    billing_address_id = Column(Integer, ForeignKey("address.id"))
    shipping_address_id = Column(Integer, ForeignKey("address.id"))

    billing_address = relationship("Address")
    shipping_address = relationship("Address")

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    billing_address_id = Column(Integer, ForeignKey("address.id"))
    shipping_address_id = Column(Integer, ForeignKey("address.id"))

    billing_address = relationship("Address", foreign_keys=[billing_address_id])    #主要就是在这里要加上foreign_keys=[]表明跟哪个外键关联
    shipping_address = relationship("Address", foreign_keys=[shipping_address_id])
