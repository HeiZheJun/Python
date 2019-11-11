#/usr/bin/python3
#-*- coding:utf-8 -*-
'''通常函数调用时按着参数的先后顺序，将实参传递给形参 ，例如调用add（1,2）时，1传递给x，2传递给y'''
'''python允许以形参赋值的方式指定将实参传递给形参'''
def add(x,y):return x+y
print(add(x='ab',y='cd'))       #通过赋值来传递参数
print(add(y='cd',x='ab'))       #通过赋值来传递参数

