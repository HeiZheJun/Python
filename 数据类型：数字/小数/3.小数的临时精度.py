#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''利用with语句创建临时上下文，临时调整精度'''
import decimal
from decimal import Decimal
with decimal.localcontext() as local:
    local.prec= 5                         #设置有效数字为5位
    print(Decimal('1')/Decimal('0.3'))

print(Decimal('1')/Decimal('0.3'))        #默认精度