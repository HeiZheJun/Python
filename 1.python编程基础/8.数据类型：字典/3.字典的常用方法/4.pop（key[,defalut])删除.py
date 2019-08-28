#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''pop删除键，并返回值，键不存在则返回default.未指定default会出错'''
x = {'name':'python'}
print(x.pop('name'))
print(x.pop('name','没有了  不要再删了'))
