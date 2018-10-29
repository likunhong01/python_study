#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/10/24 22:10'
__author__ = 'likunkun'


#一本书可以有多个作者，一个作者又可以出版多本书


from sqlalchemy import Table, Column, Integer,String,DATE, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

book_m2m_author = Table('book_m2m_author', Base.metadata,
                        Column('book_id',Integer,ForeignKey('books.id')),
                        Column('author_id',Integer,ForeignKey('authors.id')),
                        )

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    pub_date = Column(DATE)
    authors = relationship('Author',secondary=book_m2m_author,backref='books')

    def __repr__(self):
        return self.name

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))

    def __repr__(self):
        return self.name

#接下来创建几本书和作者
Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
s = Session_class()  # 生成session实例

b1 = Book(name="Python")
b2 = Book(name="Java")
b3 = Book(name="c++")
b4 = Book(name="Android")

a1 = Author(name="lkk")
a2 = Author(name="Jack")
a3 = Author(name="Rose")

b1.authors = [a1, a2]
b2.authors = [a1, a2, a3]

s.add_all([b1, b2, b3, b4, a1, a2, a3])

s.commit()



#此时，我们去用orm查一下数据
print('--------通过书表查关联的作者---------')

book_obj = s.query(Book).filter_by(name="Python").first()
print(book_obj.name, book_obj.authors)

print('--------通过作者表查关联的书---------')
author_obj = s.query(Author).filter_by(name="lkk").first()
print(author_obj.name, author_obj.books)
s.commit()


# 多对多删除
# 通过书删除作者
author_obj = s.query(Author).filter_by(name="Jack").first()
book_obj = s.query(Book).filter_by(name="Java").first()
book_obj.authors.remove(author_obj)  # 从一本书里删除一个作者
s.commit()

#直接删除作者
author_obj =s.query(Author).filter_by(name="lkk").first()
# print(author_obj.name , author_obj.books)
s.delete(author_obj)
s.commit()

'''处理中文
sqlalchemy设置编码字符集一定要在数据库访问的URL上增加charset=utf8，否则数据库的连接就不是utf8的编码格式
eng = create_engine('mysql://root:root@localhost:3306/test2?charset=utf8',echo=True)'''