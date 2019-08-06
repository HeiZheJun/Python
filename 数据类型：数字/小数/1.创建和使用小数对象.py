#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''小数对象使用decimal模块中的Decimal函数来创建'''
'''不使用小数对象缺乏精度，0.1+0.3+0.6=0.9……'''
from decimal import Decimal
print(Decimal('0.1')+Decimal('0.6')+Decimal('0.3'))

print(Decimal('0.3')-Decimal('0.1')-Decimal('0.1')-Decimal('0.1'))