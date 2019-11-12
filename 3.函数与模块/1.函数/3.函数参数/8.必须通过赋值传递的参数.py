#/usr/bin/python3
#-*- coding:utf-8 -*-
'''python允许使用必须通过赋值传递的参数，在定义函数时，带星号参数之后的参数必须通过赋值传递'''
def add(a,*b,c):
    s=a+c
    for x in b:
        s+=x
    return s
'''print(add(1,2,3))'''     #形参为使用赋值传递，报错

print(add(1,2,c=100))       #形参c使用赋值传递
print(add(1,c=100))         #带星号的形参可以省略，即传递一个空元组
