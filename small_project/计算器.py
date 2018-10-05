#coding=utf-8
#Version:python3.6.0
#Tools:Pycharm 2017.3.2
# Author:LIKUNHONG
__date__ = '2018/8/21 18:49'
__author__ = 'Colby'

import re,os,sys

def format_mark(express):
    express = express.replace('+-', '-')
    express = express.replace('-+', '-')
    express = express.replace('++', '+')
    express = express.replace('--', '+')
    express = express.replace('*+', '*')
    express = express.replace('+*', '*')
    express = express.replace('+/', '/')
    express = express.replace('/+', '/')
    return express
def com_jiajian(express):
    expr = express
    sub_expr = re.search(r"\-?\d+\.?\d*[\+\-]\d+\.?\d*", expr)
    if not sub_expr:
        return expr
    else:
        sub_expr2 = sub_expr.group()
        if len(sub_expr2.split('+')) > 1:
            n1, n2 = sub_expr2.split('+')
            result = float(n1)+float(n2)
        else:
            n1, n2 = sub_expr2.split('-')
            result = float(n1) - float(n2)
        re_sub_expr = re.sub(r"\-?\d+\.?\d*[\+\-]\d+\.?\d*", str(result), expr, count=1)
        print('�Ӽ����㣺',re_sub_expr)
        bb = com_jiajian(str(re_sub_expr))
        return bb
def com_chengchu(expr_div):
    expr=expr_div
    sub_expr = re.search(r"\d+\.?\d*[\/\*]\-?\d+\.?\d*",expr)
    if not sub_expr:
        return expr
    else:
        sub_expr2 = sub_expr.group()
        if len(sub_expr2.split('/')) > 1:
            n1, n2 = sub_expr2.split('/')
            result = float(n1)/float(n2)
        if len(sub_expr2.split('*')) > 1:
            n1, n2 = sub_expr2.split('*')
            result = float(n1)*float(n2)
        else:
            pass
        re_sub_expr=re.sub(r"\d+\.?\d*[\/\*]\-?\d+\.?\d*",str(result),expr,count=1)
        print('�˳����㣺',re_sub_expr)
        bb=com_chengchu(format_mark(re_sub_expr))
        return bb
def compute(express):
    express = com_chengchu(format_mark(express))
    express = com_jiajian(format_mark(express))
    return express
def delkuohao(express):
    res=re.compile(r'[()]')
    sub_expr1 = re.search('(\([\+\-\*\/\.0-9]+\))', express)
    if not sub_expr1:
        return express
    else:
        sub_expr1=sub_expr1.group()
        sub_expr2=sub_expr1[1:len(sub_expr1)-1]
        sub_expr3=compute(sub_expr2)
        sub_expr3 = re.sub('(\([\+\-\*\/\.0-9]+\))', str(sub_expr3),express,count=1)
        print('�������㣺',sub_expr3)
        delkuohao_expr=delkuohao(format_mark(sub_expr3))
        return delkuohao_expr
if __name__=="__main__":
    print('\n================================')
    print('\033[33m ������������\033[0m')
    print('================================')
    while True:
        express = input('\033[32m��������ʽ,�淶��Ŷ | (�˳�:q)\033[0m')
        express = re.sub('\s*', '', express)
        if len(express) == 0:
            continue
        elif express == 'q':
            sys.exit('�˳�����')
        elif re.search('[^0-9\.\-\+\*\/\(\)]',express):
            print('\033[31m ������Ч���������ʽŶ������������!!!\033[0m')
        else:
            express = express.replace(' ', '')
            print('������ı��ʽ��',express)
            '''����ɾ�����ŵĺ���'''
            express2 = delkuohao(express)
            express2 = compute(format_mark(express2))
            print('\033[31m���ʽ:%s'%express,'=', str(express2),'\033[0m')