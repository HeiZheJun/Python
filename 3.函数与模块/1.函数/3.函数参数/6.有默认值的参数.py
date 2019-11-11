#/usr/bin/python3
#-*- coding:utf-8 -*-
'''在定义函数时，可以为参数设置一个默认值。调用函数时如果未提供实参，则形参取默认值'''
def f(a,b=100):     #设置形参b默认参数为100
    return a+b
print(f(1,2))       #指定参数
print(f(1))         #形参b取默认值