#/usr/bin/python3
#-*- coding:utf-8 -*-
'''在python中所有的语句都是实施执行的，不想C/C++存在编译过程。def也是一条可执行语句
定义一个函数，所以函数的调整必须在函数定义之后'''
'''在python中，函数名也是一个变量，他引用return语句返回的值，没有返回值时，函数值为None'''
def add(x,y):
    return x+y
print(add)   #直接用函数名，可返回函数名变量的内存地址
print(add(1,4)) #调用函数

x=add           #将函数名赋值给变量
print(x(1,4))