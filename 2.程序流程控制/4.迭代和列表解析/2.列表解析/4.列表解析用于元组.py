#/usr/bin/python3
#-*- coding:utf-8 -*-
'''元组也可以用列表解析'''
z = (x for x in range(10))
print(z)
z= tuple(x*2 for x in range(5))
print(z)
z= tuple(x*2 for x in range(10) if x%2==1)
print(z)