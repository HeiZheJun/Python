#/usr/bin/python3
#-*- coding:utf-8 -*-
'''pyhton中and和or运算符总是返回运算的对象，而不是True和False'''
'''python在计算and运算时总是按着从左到右的顺序计算，在找到第一个维嘉的对象时
立即返回该对象，即使右侧还有需要计算的对象，计算都将结束，这种计算称之为短路计算
如果计算的对象都为真，则返回最后一个为真的对象'''
print(0 and 2)
print([]and 2)
print([]and{})
print(2and 5)
print(5 and 2)
