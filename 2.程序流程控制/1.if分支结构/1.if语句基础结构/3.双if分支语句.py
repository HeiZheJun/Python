#/usr/bin/python3
#-*- coding:utf-8 -*-
'''双分支语句由if和else组成'''
x = -5
if x > 0 :
    print(x,'是正数')
else:
    print(x,'不是正数')

    '''执行if语句是，python先计算表达式 x>0，计算结果为真执行if部分的语句，否则执行else部分的语句'''