#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''直接使用x=y直接赋值时x，y使用的是同一个对象，修改x，y也会改变
使用copy使用的不是一个对象，修改不会影响另一个的引用'''
x = {'name':'python'}
y = x
print(x,y)
x['name']='python3'
print(x,y)

x = {'name':'python'}
y = x.copy()
print(x,y)
x['name']='python3'
print(x,y)