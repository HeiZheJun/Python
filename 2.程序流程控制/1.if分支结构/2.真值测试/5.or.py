#/usr/bin/python3
#-*- coding:utf-8 -*-
'''or运算永阳执行短路计算，在找到第一个为真的对象时返回该对象，计算结束'''
print(0 or 2)
print(2 or [])
print(False or 5)
print([] or {})