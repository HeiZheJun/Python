#/usr/bin/python3
#-*- coding:utf-8 -*-
'''python使用def的语句来定义函数'''
'''
def 函数名（参数表）：
    函数语句块
    return 返回值
'''
'''参数和返回值都不是必须有的，python允许函数没有参数，也没有返回值'''
'''hello()函数没有参数，也无返回值，通过print（）函数打印一个字符串'''
def hello():
    print('hello world')
print(hello())
'''为函数定义两个参数，并用return语句返回两个参数的和'''
def add(x,y):
    return x+y
print(add(2,3))