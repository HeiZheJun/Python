#/usr/bin/python3
#-*- coding:utf-8 -*-
'''作用域隔离原则同样适用于函数内部的嵌套函数，在嵌套函数内适用与上层函数本地变量同名时的变量时
若该变量没有被赋值，则该变量就是上层函数本地的变量'''
def test():
    a=10                            #创建test函数的本地变量a
    def show():
        print('in show(),a=',a)     #适用test函数的本地变量a
    show()
    print('in test() a=',a)         #适用test函数的本地变量a
test()
'''在show()函数内输出a之前，为a赋值'''
def test():
    a=10                            #创建test函数的本地变量a
    def show():
        a=100                       #创建show函数的本地变量a
        print('in show(),a=',a)     #适用show函数的本地变量a
    show()
    print('in test() a=',a)         #适用test函数的本地变量a
test()
'''在嵌套函数内味变量赋值时，即使有同名的外部变量，也默认创建一个本地变量'''
'''如果在嵌套函数内部修改外部本地变量，python提供了nonlocal语句，
nonlocal语句与global语句类似，他声明变量是外部的本地变量'''
def test():
    a=10                            #创建test函数的本地变量a
    def show():
        nonlocal a                  #声明变量a是test的本地变量
        a=100                       #创建test函数的本地变量a
        print('in show(),a=',a)     #适用test函数的本地变量a
    show()
    print('in test() a=',a)         #适用test函数的本地变量a
test()