#/usr/bin/python3
#-*- coding:utf-8 -*-
'''集合也可以应用列表解析'''
z = {x for x in range(10)}
print(z)
z = {x for x in range(10) if x%2==0}
print(z)