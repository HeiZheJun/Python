#/usr/bin/python3
#-*- coding:utf-8 -*-
'''python允许将函数作为列表对象，然后通过列表索引来调用函数'''
d =[lambda a,b: a+b,lambda a,b:a-b]             #使用lambda函数建立列表
print(d[0](2,3))                                #调用第一个函数
print(d[1](2,3))                                #调用第二个函数

'''也可以使用def定义函数来创建列表'''
def add(x,y):
    return x+y

def fnc(x):
    if x==0:
        return 1
    else:
        return x*fnc(x-1)
d=[add,fnc]
print(d[0](1,2))
print(d[1](5))

'''python还允许使用字典建立函数映射'''
d = {'求和':add,'求阶乘':fnc}
print(d['求和'](1,2))
print(d['求阶乘'](5))
