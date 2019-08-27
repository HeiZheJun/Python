#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''列表是可以用列表常量或者list（）函数来创建'''
x = []
z = list()
a = [1,23,3]    #创建同类型数据的列表对象
b = ['a',123]   #创建不用类型数据的列表对象
c = list('abcd')
print(list(range(1,7)))
print(list((1,2,3)))
print(list(x+10 for x in range(1,6)))
