#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''创建元组可以用tuple()方法来创建元组'''
x = (1,2,3)
y = tuple('ABC')
print(type(x))
print(type(y))
'''包含不同类型对象的元组'''
x = (1,3,'ac',[12,3])
'''使用解析结构创建元组'''
tuple(x*2 for x in range(1,5))