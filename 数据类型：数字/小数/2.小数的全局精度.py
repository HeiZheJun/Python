#/usr/bin/python3
#-*- coding:UTF-8 -*-
from decimal import Decimal
import decimal
'''可使用decimal模块中的上下文对象设置小数的全局精度'''
'''decimal。getcontext().prec= N'''

'''用默认精度计算'''
print(Decimal('1')/Decimal('0.3'))

'''设置小数的全局精度为5位有效数字'''
decimal.getcontext().prec=5
print(Decimal('1')/Decimal('0.3'))