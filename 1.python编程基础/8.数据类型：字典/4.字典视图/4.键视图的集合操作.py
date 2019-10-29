#/usr/bin/python3
#-*- coding:utf-8 -*-
'''键视图支持各种集合运算，键值对视图和值视图不支持集合运算'''
from typing import KeysView

x={'a':1,'b':2}
print(x)                            #返回x的键视图
kx=x.keys()
print(kx)

y={'b':3,'c':4}
print(y)                            #返回y的键视图
ky=y.keys()
print(ky)

'''求差集'''
print(kx-ky)                        #求差集

print(kx|ky)                        #求并集

print(kx&ky)                        #求交集

print(kx^ky)                        #求对称差集