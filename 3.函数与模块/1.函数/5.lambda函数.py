#/usr/bin/python3
#-*- coding:utf-8 -*-
'''lambad函数也称表达式函数，用于定义一个匿名函数，可将该函数赋值给变量，通过变量调用
lambda函数定义的基本格式如下'''
'''lambda 参数表：表达式'''
add = lambda a,b:a+b        #定义表达式函数，赋值给变量
print(add(1,3))             #函数调用方式不变

'''lambda函数说明了python中的函数名就是一个变量，该变量引用了一个函数对象'''

'''lambda函数非常适合定义简单的函数，与def不同，lambda的函数体只能是一个表达式，可以调用其他函数，但是不能使用python
的其他语句'''
add = lambda a,b:ord(a)+ord(b)
print(add('1','2'))