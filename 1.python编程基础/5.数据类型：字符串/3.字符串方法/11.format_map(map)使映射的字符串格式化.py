#/usr/bin/python
#-*- coding:UTF-8 -*-
'''使用映射完成字符串格式化 '''
'''格式 "this is {x} one {xx}.format_map({'x':'y','xx':'yy'})'''
print('My name is {name}, ags is {ags}'.format_map({'name':'azhe','ags':22}))