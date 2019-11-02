#/usr/bin/python3
#-*- coding:utf-8 -*-
'''map函数用于将函数映射到可迭代对象，对可迭代对象中的每个元素应该用该函数'''
'''函数返回值包含在生成的map对象中'''
x = map(ord,'abc')          #使用ord返回各个字符的ASCII吗，生成map对象
print(next(x))
print(next(x))
print(next(x))

y =list(map(ord,'abc'))     #用map对象生成列表
print(y)