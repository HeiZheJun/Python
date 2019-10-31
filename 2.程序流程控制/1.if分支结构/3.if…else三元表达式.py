#/usr/bin/python3
#-*- coding:utf-8 -*-
x = 5
y = 10
if x>y:
    a=x
else:
    a=y
'''简化为下面的三元表达式'''
a=x if x>y else y
print(a)