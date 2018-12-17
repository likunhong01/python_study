#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/7/30 19:14'
__author__ = 'Colby'

# f =open("testWenJian",'r',encoding='utf-8')
# print(f.read())


#测试r+
# f = open("testWenJian",'r+',encoding='utf-8')
# # f.write("\n111")
#
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.write('新的')


#迭代器读文件行
# for index,line in enumerate(f.readlines()):
#     if index == 2:
#         print('--------------------------------')
#         continue
#     print(line.strip())


#读第一个文件，修改写入第二个文件
f = open("testWenJian",'r',encoding='utf-8')
f_new = open('NewtestWenJian','w',encoding='utf-8')

for line in f:
    if '新的' in line:
        line = line.replace('新的','又来一次新的')
    f_new.write(line)
f.close()
f_new.close()






#水仙花数
# for i in range(100,999):
#     a = (int)(i % 10)
#     b = (int)(i / 10 % 10)
#     c = (int)(i/ 100 % 10)
#     if a*a*a+b*b*b+c*c*c == i:
#         print(a,b,c,i)

#大小转小写，小写转大写

ch = 'a'

if 'a' <= ch <= 'z':
    ch += 32
else:
    ch -= 32



