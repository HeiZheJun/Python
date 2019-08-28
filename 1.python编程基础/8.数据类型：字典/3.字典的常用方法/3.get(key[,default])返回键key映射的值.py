#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''返回键key映射的值，如果key不存在，返回空值，可以使用default指定不存在键的返回值'''
x = {'name':'python'}
print(x.get('name'))
print(x.get('times'))
print(x.get('times','不存在'))