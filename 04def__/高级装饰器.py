#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG


#只有本地验证
'''
user = 'li'
passsd = '123'

def sure(func):
    def wrapper(*args,**kwargs):
        username = input("用户名:").strip() #strip用来去除首位空格和换行符之类的无效符号
        password = input("密码:").strip()

        if user == username and passsd ==password:
            return func(*args,**kwargs) #这里的return是当func表示的函数有返回值的时候，返回同样的值
        else:
            exit('账号密码错误')
    return wrapper

#索引直接进入，后面的主页面和属性界面需要验证
def index():
    print('到了索引界面')

@sure(sureType = 'local')
def home():
    print('到了主界面')
    return 'home'

@sure(sureType = 'local')
def power():
    print('到了属性界面')

index()
home()
power()
'''


#增加需求，本地和网络验证装饰器写法
user = 'li'
passsd = '123'

#在套一层函数就好了
def sure(sureType): #这里传入的值就是装饰器传进来的
    def outer(func):    #之前的func传到这里来了
        def wrapper(*args, **kwargs):
            if sureType == 'local': #到这里在修改判断本地和网络的代码
                username = input("用户名:").strip()
                password = input("密码:").strip()

                if user == username and passsd == password:
                    return func(*args, **kwargs)
                else:
                    exit('账号密码错误')
            elif sureType == 'web':
                print('网络验证不会写，直接通过')
                return func(*args, **kwargs)
            else:
                exit('还没开发的验证类别，直接退出')
        return wrapper
    return outer

#索引直接进入，后面的主页面和属性界面需要验证
def index():
    print('到了索引界面')

@sure(sureType = 'local')
def home():
    print('到了主界面')
    return 'home'

@sure(sureType = 'web')
def power():
    print('到了属性界面')

index()
home()
power()