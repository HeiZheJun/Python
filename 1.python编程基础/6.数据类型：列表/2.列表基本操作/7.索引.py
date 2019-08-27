#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''列表与字符串类似可以通过对象在列表的位置来索引
列表对象也可以通过索引进行修改'''
x = list(range(0,10))
print(x[0])
print(x[1])
print(x[-1])
x[1]= 'acg'
print(x[1])
print(x)